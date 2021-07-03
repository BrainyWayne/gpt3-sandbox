import os
import sys


sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from api import demo_web_app
from api import GPT, Example, UIConfig

# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100)

gpt.add_example(Example("2+2", "4"))
gpt.add_example(Example("5+5", "10"))
gpt.add_example(Example("-2+3", "1"))
gpt.add_example(Example("4*5", "20"))
gpt.add_example(Example("15/3", "5"))

config = UIConfig(description="Perform arithmetic operation",
                  button_text="Perform", placeholder="2+2")

demo_web_app(gpt, config)
