import hashlib
import asyncio
import os
from shade_agent import (
    agent,
    agent_account_id,
    agent_info,
    agent_call,
    agent_view,
    request_signature,
    SignatureKeyType
)


async def test_agent_account_id():
    res = await agent_account_id()
    print(res)


async def test_agent_info():
    res = await agent_info()
    print(res)


async def test_add_key_not_allowed():
    res = await agent('addKey', {})
    print(res)


async def test_get_state():
    res = await agent('getState')
    print(res)


async def test_get_balance():
    res = await agent('getBalance')
    print(res)


async def test_view():
    account_id = (await agent_account_id())['accountId']
    
    res = await agent_view({
        'methodName': 'get_agent',
        'args': {'account_id': account_id}
    })
    print(res)


async def test_call():
    path = 'foo'
    payload = hashlib.sha256(b'testing').hexdigest()
    
    res = await agent_call({
        'methodName': 'request_signature',
        'args': {
            'path': path,
            'payload': payload,
            'key_type': 'Eddsa'
        }
    })
    print(res)


async def test_sign():
    path = 'foo'
    payload = hashlib.sha256(b'testing').hexdigest().zfill(2)
    
    res = await request_signature(path, payload)
    print(res)


async def test_sign_eddsa():
    path = 'foo'
    payload = hashlib.sha256(b'testing').hexdigest().zfill(2)
    
    res = await request_signature(path, payload, 'Eddsa')
    print(res)


async def run():
    # Retry test_agent_info() until it succeeds
    if os.getenv('ENV') == 'production':
        print("Running on Phala Cloud")
        print("Testing agent_info() until it succeeds...", flush=True)
        while True:
            try:
                await test_agent_info()
                print("agent_info() test succeeded!", flush=True)
                break
            except Exception as e:
                print(f"agent_info() failed: {e}", flush=True)
                print("Retrying in 1 second...", flush=True)
                await asyncio.sleep(1)
    else:
        print("Running locally")

    print("Running tests...", flush=True)
    # Now run all other tests
    try:
        print("Running test_agent_account_id...", flush=True)
        await test_agent_account_id()
        
        print("Running test_agent_info...", flush=True)
        await test_agent_info()
        
        print("Running test_add_key_not_allowed...", flush=True)
        await test_add_key_not_allowed()
        
        print("Running test_get_state...", flush=True)
        await test_get_state()
        
        print("Running test_get_balance...", flush=True)
        await test_get_balance()
        
        print("Running test_view...", flush=True)
        await test_view()
        
        print("Running test_call...", flush=True)
        await test_call()
        
        print("Sleeping for 2 seconds...", flush=True)
        await asyncio.sleep(2)
        
        print("Running test_sign...", flush=True)
        await test_sign()
        
        print("Sleeping for 2 seconds...", flush=True)
        await asyncio.sleep(2)
        
        print("Running test_sign_eddsa...", flush=True)
        await test_sign_eddsa()
                
    except Exception as e:
        print(f"Test failed with error: {e}", flush=True)


if __name__ == "__main__":
    asyncio.run(run())
