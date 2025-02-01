from typing import List
import os


class Tools:
    def __init__(self):
        self.file_handler = True  # prevents default RAG pipeline
        self.citation = True
        pass

    def chat_with_csv(
        self, __messages__: List[dict] = [], __files__: List[dict] = []
    ) -> str:
        """
        This function will take the data frame from taken init file and pass it to interact with pandasAI
        """
        try:
            import pandasai as pai

            PANDAS_AI_API_KEY = os.getenv("PANDAS_AI_API_KEY", "")

            pai.api_key.set(PANDAS_AI_API_KEY)

            df = pai.read_csv(
                "/app/backend/data/uploads/"
                + __files__[-1]["file"]["id"]
                + "_"
                + __files__[-1]["file"]["filename"]
            )

            res = df.chat(__messages__[-1]["content"])

            print(res)

            return (
                """Here is the result to the csv prompt: return it to the user and cite the file name. The result is:
            """
                + str(res)
                + """and the file name is: """
                + __files__[-1]["file"]["filename"]
            )
        except Exception as e:
            print("error", e)
