import json
import os
import boto3
from datetime import datetime

def lambda_handler(event, context):
    
    sagemaker = boto3.client('sagemaker')
    
    # Định nghĩa thông tin huấn luyện

    estimator = {
        'training_job_name': 'decision-test-000',
        'image_uri': '{account-id}.dkr.{region}.amazonaws.com/decision-tree:latest',
        'role': 'arn:aws:iam::{account-id}:role/create-decision-tree-sagemaker-training-job-role',
        'instance_count': 1,
        'instance_type': 'ml.m5.large',
        'input_data_path': 's3://customized-sagemaker-image-decision-tree-bucket/input/dataset/',
        'input_model_path': 's3://customized-sagemaker-image-decision-tree-bucket/input/model/',
        'output_path': 's3://customized-sagemaker-image-decision-tree-bucket/output',
        'volumn_size_in_GB': 30,
        'max_runtime_in_second': 3600
    }
    
    print(estimator)
    
    # Thực hiện huấn luyện
    try:
        training_job_name = f"{estimator['training_job_name']}"
        response = sagemaker.create_training_job(
            TrainingJobName=training_job_name,
            AlgorithmSpecification={
                'TrainingImage': estimator['image_uri'],
                'TrainingInputMode': 'File'
            },
            RoleArn=estimator['role'],
            InputDataConfig=[
                {
                    'ChannelName': 'dataset',
                    'DataSource': {
                        'S3DataSource': {
                            'S3DataType': 'S3Prefix',
                            'S3Uri': estimator['input_data_path'],
                            'S3DataDistributionType': 'ShardedByS3Key'
                        }
                    }
                },
                {
                    'ChannelName': 'model',
                    'DataSource': {
                        'S3DataSource': {
                            'S3DataType': 'S3Prefix',
                            'S3Uri': estimator['input_model_path'],
                            'S3DataDistributionType': 'FullyReplicated'
                        }
                    }
                },
            ],
            OutputDataConfig={
                'S3OutputPath': estimator['output_path']
            },
            ResourceConfig={
                'InstanceType': estimator['instance_type'],
                'InstanceCount': estimator['instance_count'],
                'VolumeSizeInGB': estimator['volumn_size_in_GB']
            },
            StoppingCondition={
                'MaxRuntimeInSeconds': estimator['max_runtime_in_second']
            }
        )
        print(response)
        
        return {
            'status': 'InProgress'
        }
    
    except Exception as e:
        print(e)
        return {
            'status': json.dumps({'error': str(e)})
        }
