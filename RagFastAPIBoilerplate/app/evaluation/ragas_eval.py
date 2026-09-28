from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy
from datasets import Dataset

# this is a standalone script we can run periodically to grade our RAG
def run_evaluation():
    # dummy data for example
    data = {
        "question": ["what is fastapi?"],
        "answer": ["FastAPI is a web framework for Python."],
        "contexts": [["FastAPI is a modern web framework."]],
        "ground_truth": ["FastAPI is a Python web framework."]
    }
    
    dataset = Dataset.from_dict(data)
    
    # grading our ai on how accurate and relevant it is
    result = evaluate(
        dataset,
        metrics=[faithfulness, answer_relevancy]
    )
    
    print("\n[RAGAS EVALUATION RESULT]")
    print(result)

if __name__ == "__main__":
    run_evaluation()
