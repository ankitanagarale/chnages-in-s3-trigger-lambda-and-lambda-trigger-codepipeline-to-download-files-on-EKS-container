import boto3
import os

def lambda_handler(event, context):
    codepipeline = boto3.client('codepipeline')
    
    pipeline_name = "<pipeline_name>"
    
    try:
        response = codepipeline.start_pipeline_execution(name=pipeline_name)
        return {
            'statusCode': 200,
            'body': f'Successfully triggered pipeline: {pipeline_name}',
            'executionId': response['pipelineExecutionId']
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Failed to trigger pipeline: {str(e)}'
        }
