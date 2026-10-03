from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


def main():
    with sync_playwright() as p:

        # Keep False first so you can watch the browser.
        # After testing, change to True.
        browser = p.chromium.launch(headless=False)

        page = browser.new_page(
            viewport={"width": 1400, "height": 900}
        )

        try:
            print("Opening Cricbuzz...")

            page.goto(
                "https://www.cricbuzz.com/",
                wait_until="domcontentloaded",
                timeout=30000
            )

            # --------------------------------------------------
            # IMPORTANT:
            # Inspect Cricbuzz and verify/update this selector.
            # The assignment expects you to find the selector.
            # --------------------------------------------------

            score_selector = ".cb-ovr-flo"

            try:
                # Playwright waits for the actual element instead
                # of using a fixed time.sleep().
                page.wait_for_selector(
                    score_selector,
                    state="visible",
                    timeout=10000
                )

                # Get visible matching elements.
                score_elements = page.locator(score_selector)

                count = score_elements.count()

                score_found = False

                for i in range(count):
                    text = score_elements.nth(i).inner_text().strip()

                    # Look for text that resembles a cricket score.
                    if "/" in text or "Ov" in text:
                        print("\nLIVE CRICKET SCORE")
                        print("------------------")
                        print(text)

                        score_found = True
                        break

                if not score_found:
                    print("\nNo live cricket score found right now.")

            except PlaywrightTimeoutError:
                print("\nNo live match is currently visible.")

            # --------------------------------------------------
            # Screenshot
            # --------------------------------------------------

            page.screenshot(
                path="/Users/cmuthukumaran2/Documents/GenAI/Python/score.png",
                full_page=True
            )

            print("\nSaved screenshot: score.png")

        except Exception as error:
            print("\nSomething went wrong:")
            print(error)

            # Helpful debugging screenshot
            page.screenshot(
                path="score.png",
                full_page=True
            )

        finally:
            browser.close()


if __name__ == "__main__":
    main()