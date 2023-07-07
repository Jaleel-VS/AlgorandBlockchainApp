# Program for sending Evidence to s3 bucket
import boto3
from fastapi import APIRouter, UploadFile, HTTPException, status
from models.evidence import Evidence
from services.transaction import Transaction
from services.utils import get_hash
import json

evidence_router = APIRouter()
s3_resource = boto3.resource('s3') # What this does is it indicates which service(s) you are going to use. This one basically says "Let's use amazon s3"

# Helping methods
async def s3_upload(contents: bytes, key: str):
    s3_resource.Bucket('fairchancedocketbucket').put_object(Key=key, Body=contents)