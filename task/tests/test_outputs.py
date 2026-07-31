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
    
    # Test invalid input
    result = subprocess.run(['python3', '/app/factorial.py', 'abc'], capture_output=True, text=True)
    assert result.returncode != 0
