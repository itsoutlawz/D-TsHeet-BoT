# Simplify Formatting - Remove Fancy Features

## Problem
```
APIError: [400]: Range (ProfilesTarget!A10002) exceeds grid limits. Max rows: 10000
```

The fancy formatting (banding, column widths, alignment) is causing too many API calls and exceeding grid limits.

## Solution
Remove all fancy formatting. Keep only:
- ✅ Bold headers
- ✅ Orange header color
- ❌ Remove: Banding (alternating colors)
- ❌ Remove: Column widths
- ❌ Remove: Cell alignment
- ❌ Remove: Background colors for data rows

## Changes to Make

### In Scraper.py, replace the entire `_format()` method with:

```python
def _format(self):
    # Simple formatting: headers only with bold + orange color
    try:
        # ProfilesTarget header
        self.ws.format(
            "A1:R1",
            {
                "textFormat": {"bold": True, "fontSize": 9},
                "backgroundColor": {"red":1.0,"green":0.7,"blue":0.2}
            }
        )
    except Exception as e:
        log_msg(f"ProfilesTarget format failed: {e}")

    # Target header
    try:
        self.target.format(
            "A1:E1",
            {
                "textFormat": {"bold": True, "fontSize": 9},
                "backgroundColor": {"red":1.0,"green":0.7,"blue":0.2}
            }
        )
    except Exception as e:
        log_msg(f"Target format failed: {e}")

    # Dashboard header
    try:
        self.dashboard.format(
            "A1:K1",
            {
                "textFormat": {"bold": True, "fontSize": 9},
                "backgroundColor": {"red":1.0,"green":0.7,"blue":0.2}
            }
        )
    except Exception as e:
        log_msg(f"Dashboard format failed: {e}")

    # Tags header
    try:
        if self.tags_sheet:
            self.tags_sheet.format(
                "A1:D1",
                {
                    "textFormat": {"bold": True, "fontSize": 9},
                    "backgroundColor": {"red":1.0,"green":0.7,"blue":0.2}
                }
            )
    except Exception as e:
        log_msg(f"Tags format failed: {e}")
```

## Also disable these methods (they're no longer needed):

Replace their bodies with `pass`:

```python
def _set_column_widths(self, sheet, col_widths):
    """Disabled - removed to reduce API calls"""
    pass

def _apply_banding(self, sheet, end_col, start_row=1):
    """Disabled - removed to reduce API calls"""
    pass
```

## Result

- ✅ Reduced API calls (fewer formatting requests)
- ✅ No more grid limit errors
- ✅ Headers still look good (bold + orange)
- ✅ Data is readable and organized
- ✅ Bot runs faster

## Before vs After

**Before**: 
- Column widths
- Banding (alternating colors)
- Alignment (CENTER)
- Background colors
- ~20+ API calls for formatting

**After**:
- Bold headers
- Orange header color
- ~4 API calls for formatting

