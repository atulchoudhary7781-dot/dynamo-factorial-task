import subprocess

def test_factorial_calculation():
    # Test normal case
    result = subprocess.run(['python3', '/app/factorial.py', '5'], capture_output=True, text=True)
    assert result.stdout.strip() == '120'
    assert result.returncode == 0
    
    # Test edge case
    result = subprocess.run(['python3', '/app/factorial.py', '0'], capture_output=True, text=True)
    assert result.stdout.strip() == '1'
    assert result.returncode == 0
    
    # Test invalid inputs
    result = subprocess.run(['python3', '/app/factorial.py', 'abc'], capture_output=True, text=True)
    assert result.returncode != 0
    
    result = subprocess.run(['python3', '/app/factorial.py', '-5'], capture_output=True, text=True)
    assert result.returncode != 0
    
    # Test output file creation
    import os
    assert os.path.exists('/app/output.txt')
    
    # Test output file content
    with open('/app/output.txt') as f:
        content = f.read().strip()
        assert content.isdigit()  # Verify only numeric output
