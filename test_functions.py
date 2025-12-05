#!/usr/bin/env python3
"""
Test script to verify all functions in Scraper.py work correctly
"""
import sys
import os
from datetime import datetime, timedelta, timezone

# Add the parent directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import functions from Scraper
from Scraper import (
    get_pkt_time,
    log_msg,
    column_letter,
    clean_data,
    convert_relative_date_to_absolute,
    detect_suspension_reason,
    calculate_eta,
    clean_text,
    parse_post_timestamp,
    to_absolute_url,
    extract_text_comment_url,
    extract_image_comment_url,
    AdaptiveDelay,
)

def test_get_pkt_time():
    """Test PKT time function"""
    print("\n[OK] Testing get_pkt_time()...")
    t = get_pkt_time()
    assert isinstance(t, datetime), "Should return datetime object"
    print(f"  Current PKT time: {t}")

def test_column_letter():
    """Test column letter conversion"""
    print("\n[OK] Testing column_letter()...")
    assert column_letter(0) == "A", "Column 0 should be A"
    assert column_letter(25) == "Z", "Column 25 should be Z"
    assert column_letter(26) == "AA", "Column 26 should be AA"
    print(f"  column_letter(0) = {column_letter(0)}")
    print(f"  column_letter(25) = {column_letter(25)}")
    print(f"  column_letter(26) = {column_letter(26)}")

def test_clean_data():
    """Test data cleaning"""
    print("\n[OK] Testing clean_data()...")
    assert clean_data("No city") == "", "Should remove 'No city'"
    assert clean_data("  test  ") == "test", "Should trim whitespace"
    assert clean_data("test  data") == "test data", "Should normalize spaces"
    print(f"  clean_data('No city') = '{clean_data('No city')}'")
    print(f"  clean_data('  test  ') = '{clean_data('  test  ')}'")

def test_convert_relative_date():
    """Test relative date conversion"""
    print("\n[OK] Testing convert_relative_date_to_absolute()...")
    result = convert_relative_date_to_absolute("2 days ago")
    assert result != "2 days ago", "Should convert relative date"
    print(f"  '2 days ago' -> '{result}'")
    
    result = convert_relative_date_to_absolute("1 hour ago")
    assert result != "1 hour ago", "Should convert relative date"
    print(f"  '1 hour ago' -> '{result}'")

def test_detect_suspension():
    """Test suspension detection"""
    print("\n[OK] Testing detect_suspension_reason()...")
    result = detect_suspension_reason("accounts suspend kiye")
    assert result is not None, "Should detect suspension"
    print(f"  Detected: {result}")
    
    result = detect_suspension_reason("normal content")
    assert result is None, "Should not detect suspension"
    print(f"  Normal content: {result}")

def test_calculate_eta():
    """Test ETA calculation"""
    print("\n[OK] Testing calculate_eta()...")
    import time
    start = time.time()
    time.sleep(0.1)
    eta = calculate_eta(5, 100, start)
    assert isinstance(eta, str), "Should return string"
    print(f"  ETA for 5/100 processed: {eta}")

def test_clean_text():
    """Test text cleaning"""
    print("\n[OK] Testing clean_text()...")
    result = clean_text("  hello\n  world  ")
    assert result == "hello world", "Should clean text"
    print(f"  Result: '{result}'")

def test_to_absolute_url():
    """Test URL conversion"""
    print("\n[OK] Testing to_absolute_url()...")
    assert to_absolute_url("/profile/test") == "https://damadam.pk/profile/test"
    assert to_absolute_url("profile/test") == "https://damadam.pk/profile/test"
    assert to_absolute_url("https://example.com") == "https://example.com"
    print(f"  '/profile/test' -> {to_absolute_url('/profile/test')}")

def test_extract_urls():
    """Test URL extraction"""
    print("\n[OK] Testing extract_text_comment_url() and extract_image_comment_url()...")
    text_url = extract_text_comment_url("/comments/text/12345/")
    assert "12345" in text_url, "Should extract ID"
    print(f"  Text URL: {text_url}")
    
    img_url = extract_image_comment_url("/comments/image/67890/")
    assert "67890" in img_url, "Should extract ID"
    print(f"  Image URL: {img_url}")

def test_adaptive_delay():
    """Test adaptive delay class"""
    print("\n[OK] Testing AdaptiveDelay class...")
    delay = AdaptiveDelay(0.1, 0.5)
    assert delay.min_delay == 0.1
    assert delay.max_delay == 0.5
    
    delay.on_success()
    print(f"  After success: min={delay.min_delay:.2f}, max={delay.max_delay:.2f}")
    
    delay.on_rate_limit()
    print(f"  After rate limit: min={delay.min_delay:.2f}, max={delay.max_delay:.2f}")
    
    delay.on_batch()
    print(f"  After batch: min={delay.min_delay:.2f}, max={delay.max_delay:.2f}")

def main():
    print("="*60)
    print("[TEST] Testing Scraper.py Functions")
    print("="*60)
    
    try:
        test_get_pkt_time()
        test_column_letter()
        test_clean_data()
        test_convert_relative_date()
        test_detect_suspension()
        test_calculate_eta()
        test_clean_text()
        test_to_absolute_url()
        test_extract_urls()
        test_adaptive_delay()
        
        print("\n" + "="*60)
        print("[PASS] All tests passed!")
        print("="*60)
        return 0
    except AssertionError as e:
        print(f"\n[FAIL] Test failed: {e}")
        return 1
    except Exception as e:
        print(f"\n[ERROR] Error: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    sys.exit(main())
