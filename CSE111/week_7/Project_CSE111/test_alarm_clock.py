import pytest
from unittest.mock import MagicMock, patch
from alarm_clock import setalarm, alarmclock


def test_setalarm(monkeypatch, capsys):

    # Mocking hrs.get(), mins.get(), and secs.get()
    monkeypatch.setattr('alarm_clock.hrs.get', MagicMock(return_value='10'))
    monkeypatch.setattr('alarm_clock.mins.get', MagicMock(return_value='30'))
    monkeypatch.setattr('alarm_clock.secs.get', MagicMock(return_value='00'))
    
    # Mocking alarmclock method
    mock_alarmclock = MagicMock()
    monkeypatch.setattr('alarm_clock.alarmclock', mock_alarmclock)
    
    # Calling setalarm function
    setalarm()
    
    # Capturing printed output 
    captured = capsys.readouterr()
    
    # Assertions
    assert captured.out.strip() == '10:30:00'  # Checking if the alarmtime is printed correctly
    mock_alarmclock.assert_called_once_with('10:30:00')  # Checking if alarmclock method is called with correct argument


# Mock datetime module
@patch('alarm_clock.datetime')
# Mock time.sleep
@patch('alarm_clock.time')

def test_alarmclock(mock_time, mock_datetime):

    # Set the return value for strftime function of datetime module
    mock_datetime.datetime.now.return_value.strftime.return_value = "08:00:00"
    # Set the alarmtime
    alarmtime = "08:00:00"

    # Call the function
    alarmclock(alarmtime, max_iterations=1)  

    # Assert that time.sleep is called once
    mock_time.sleep.assert_called_once_with(1)



pytest.main(["-v", "--tb=line", "-rN", __file__])