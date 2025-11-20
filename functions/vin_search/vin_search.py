import json
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    logger.info("VIN Search Function 호출됨")
    
    vin = 'N/A'
    if event.get('queryStringParameters'):
        vin = event['queryStringParameters'].get('vin') 

    if not vin:
        logger.warning("VIN이 제공되지 않음")
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'VIN 번호를 Query Parameter로 제공해야 합니다.'})
        }

    logger.info(f"검색할 VIN: {vin}")
    
    # 임시 Mock 데이터로 대체
    if vin and vin.endswith("12345678"):
        result_data = {
            "vin": vin,
            "found": True,
            "model": "Genesis GV80 (2024)",
            "vessel": "GLOVIS ACE",
            "eta": "2025-12-25",
            "port": "Incheon, KR",
            "albumUrl": "https://photos.app.goo.gl/example-photo-link"
        }
        status_code = 200
    else:
        result_data = {
            "vin": vin,
            "found": False,
            "message": "해당 VIN에 대한 정보를 찾을 수 없습니다."
        }
        status_code = 404
    
    return {
        'statusCode': status_code,
        'headers': { 
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(result_data, ensure_ascii=False)
    }
