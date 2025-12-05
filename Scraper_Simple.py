# This is a patch file - copy the _format method from here to replace the one in Scraper.py

# REPLACE THIS METHOD IN Scraper.py:
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
