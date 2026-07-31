import subprocess
import sys
from pathlib import Path

def test_factorial_calculation():
    # Get the path to the factorial script using Path for cross-platform compatibility
    factorial_script = str(Path('task/solution/factorial.py').resolve())
    
    # Test normal case
    result = subprocess.run([sys.executable, factorial_script, '5'], capture_output=True, text=True)
    assert result.stdout.strip() == '120'
    assert result.returncode == 0
    
    # Test edge case
    result = subprocess.run([sys.executable, factorial_script, '0'], capture_output=True, text=True)
    assert result.stdout.strip() == '1'
    assert result.returncode == 0
    
    # Test invalid inputs
    result = subprocess.run([sys.executable, factorial_script, 'abc'], capture_output=True, text=True)
    assert result.returncode != 0
    
    result = subprocess.run([sys.executable, factorial_script, '-5'], capture_output=True, text=True)
    assert result.returncode != 0
    
    # Test output file creation (skip in local tests)
    # import os
    # assert os.path.exists('/app/output.txt')
    # 
    # # Test output file content
    # with open('/app/output.txt') as f:
    #     content = f.read().strip()
    #     assert content.isdigit()  # Verify only numeric output
