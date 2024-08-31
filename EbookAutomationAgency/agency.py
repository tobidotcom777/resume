from agency_swarm import Agency
from EbookGenerationAgent import EbookGenerationAgent
from AdsSetupAgent import AdsSetupAgent
from PaymentIntegrationAgent import PaymentIntegrationAgent
from Devid import Devid
from EbookCEO import EbookCEO

ceo = EbookCEO()
dev = Devid()
payment = PaymentIntegrationAgent()
ads = AdsSetupAgent()
ebook = EbookGenerationAgent()

agency = Agency([ceo, [ceo, dev],
                 [ceo, payment],
                 [ceo, ads],
                 [ceo, ebook]],
                shared_instructions='./agency_manifesto.md',  # shared instructions for all agents
                max_prompt_tokens=25000,  # default tokens in conversation for all agents
                temperature=0.3,  # default temperature for all agents
                )

if __name__ == '__main__':
    agency.demo_gradio()