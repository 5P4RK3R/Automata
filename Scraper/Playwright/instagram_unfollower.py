import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://www.instagram.com/accounts/login/")
        inpEmail = '//input[@type="email"]'
        inpPassword = '//input[@type="password"]'
        inpSubmit = '//input[@type="submit"]'
        await page.locator(inpEmail).fill('mahendransparker@gmail.com')
        await page.locator(inpPassword).fill('gojuryu45')
        await page.locator(inpSubmit).click()
        print(await page.title())
        await browser.close()

asyncio.run(main())