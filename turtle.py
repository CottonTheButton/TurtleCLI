#!/usr/local/bin/python3
import requests
import math
import webbrowser


from bs4 import BeautifulSoup


def corona():
    req = requests.get("https://virusncov.com/")
    source = req.content
    soup = BeautifulSoup(source, "html.parser")

    total_cases_broad = soup.find("h2")
    total_cases = total_cases_broad.find("span")
    death_cases_broad = soup.find(class_="second-count mt-large")
    death_cases = death_cases_broad.find(class_="red-text")
    recovery_cases_broad = soup.find(class_="second-count mt-large")
    recovery_cases = recovery_cases_broad.find(class_="green-text")

    currently_infected_broad = soup.find(class_="firt-div")
    currently_infected = currently_infected_broad.find("span")
    mild_condition = soup.find(class_="pupp-text")
    serious_cases = soup.find(class_="red-text")

    closed_cases_broad = soup.find(class_="firt-div")
    closed_cases = closed_cases_broad.find("span")

    print(f"{soup.find('small').get_text()}\n")

    print(f"Total cases: {total_cases.get_text()}")
    print(f"Closed Cases:{closed_cases.get_text()} cases closed (out of {total_cases.get_text()}).")
    print(f"Number of deaths: {death_cases.get_text()}")
    print(f"Numer of recoveries: {recovery_cases.get_text()}\n")

    print("Active Cases:")
    print(f"There are {currently_infected.get_text()} patients that are currently infected.")
    print(f"{mild_condition.get_text()} are in a not-so-serious condition")
    print(f"{serious_cases.get_text()} are in a serious condition.\n")


def docs(docs_name, search_entry):

    if docs_name == "html":
        webbrowser.open(f"https://developer.mozilla.org/en-US/docs/Web/HTML/Element/{search_entry}")

    elif docs_name == "css":
        webbrowser.open("https://developer.mozilla.org/en-US/docs/Web/CSS")


def factorial(num):

    print(f"The answer is {math.factorial(int(num))}")


def file_alphabetize(file_name, rev):
    with open(file_name, 'r') as file:
        sort = file.readlines()

        if rev == "no":
            for entry in sorted(sort):
                print(entry, end="")
        else:
            for entry in sorted(sort, reverse=True):
                print(entry, end="")


def read(file_name):
    file = open(file_name, 'r')
    print(file.read())


def reddit(subreddit_name):
    webbrowser.open(f"https://reddit.com/r/{subreddit_name}")


def ruqqus(guild_name):
    webbrowser.open(f"https://ruqqus.com/+{guild_name}")


def stocks(company_name):
    req = requests.get(f"https://money.cnn.com/quote/quote.html?symb={company_name}")
    source = req.content
    src = BeautifulSoup(source, 'html.parser')

    stock_price_broad = src.find(class_="wsod_last")
    stock_price = stock_price_broad.find("span")

    price_change = src.find(class_="posData")

    cmpny_name = src.find(class_="wsod_fLeft")

    last_updated_potato = src.find(class_="wsod_quoteLabelAsOf") # Start with the sixth index
    last_updated_pot = last_updated_potato.get_text()
    last_updated = last_updated_pot[6:]

    print(f"{company_name} Stock Information")
    print(f"{cmpny_name.get_text()}")
    print(f"Stock price as of {last_updated}")
    print(f"${stock_price.get_text()}")
    print(f"Today's change: ")
    print(f"{price_change.get_text()}")
    print("Stock data acquired from https://money.cnn.com (◕‿◕✿)")


def f_wikipedia():
    pass
