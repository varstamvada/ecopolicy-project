import os
import csv
import openai


# 1) Method to read all files starting with "BILLS" from a given folder
#    and return a list of tuples: [(filename, file_text), ...]
def extract_texts_from_bills(folder_path):
    extracted_texts = []
    for filename in os.listdir(folder_path):
        if filename.startswith("BILLS"):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    text_content = f.read()
                extracted_texts.append((filename, text_content))
    return extracted_texts


# 2) Method to send each file's text to ChatGPT (GPT-4) with the specified prompt
#    Returns a list of tuples: [(filename, score), ...]
def analyze_texts_with_gpt4(texts_list, api_key):
    openai.api_key = api_key  # Set your OpenAI API key
    results = []

    # Our prompt: "analyze the text ... Just output the final score and nothing else"
    base_prompt = (
        "analyze the text and tell me as an environmentalist if this text is "
        "good for the environment on a scale of 0 through 10, 10 being good and 0 being bad. "
        "Just output good or bad and final score and nothing else"
    )

    for filename, content in texts_list:
        try:
            #response = openai.ChatCompletion.create(
            #    model="gpt-4",
            #    messages=[
            #        {"role": "system", "content": "You are a helpful assistant."},
            #        {"role": "user", "content": f"{base_prompt}\n\nText:\n{content}"}
            #    ],
            #    temperature=0  # for more predictable outputs
            #)
            # Extract the model's reply (should be just the number)
            #reply = response.choices[0].message.content.strip()
            response = openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": "analyze the text and tell me as an environmentalist if this text is good for the environment or bad for the environment. Give a response on a scale of 0 through 10, "
                                        "10 being good,0 is bad. Only respond with the score and nothing else\n\n,full_text" + content
                            }
                        ]
                    },
                ],
                response_format={
                    "type": "text"
                },
                temperature=1,
                max_completion_tokens=500,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            print(response.choices[0].message)
            print(response)
            reply = response.choices[0].message.content.strip()
            print(reply)
            results.append((filename, reply))
        except Exception as e:
            # If there's an error, store a placeholder or handle as needed
            results.append((filename, f"Error: {str(e)}"))
    return results


# 3) Method to save filename & score to a CSV file
def save_scores_to_csv(score_data, csv_path):
    with open(csv_path, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        print("filename")
        writer.writerow(["filename", "score"])
        for filename, score in score_data:
            writer.writerow([filename, score])


# Example main usage
if __name__ == "__main__":
    # Replace these paths and API key as appropriate
    folder_with_bills = "analyzebills"
    output_csv_file = "output_scores.csv"
    my_api_key = "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"

    # Step 1: Extract the text from all BILLS* files
    bills_texts = extract_texts_from_bills(folder_with_bills)

    # Step 2: Analyze each file’s content with GPT-4
    scores = analyze_texts_with_gpt4(bills_texts, my_api_key)

    # Step 3: Save results to CSV
    save_scores_to_csv(scores, output_csv_file)
    print(f"Done! Scores have been saved to {output_csv_file}")
