from fastapi import APIRouter
from backend.app.schemas.query import QueryRequest, QueryResponse
from backend.app.services.retrieval import retrieve_chunks
from backend.app.services.generation import generate_answer

router = APIRouter()


@router.post("/query", response_model=QueryResponse)
def query_dreamscape(request: QueryRequest):
    retrieved_chunks = retrieve_chunks(request.question)
    answer = generate_answer(request.question, retrieved_chunks)

    sources = []
    for chunk in retrieved_chunks:
        if chunk["source"] not in sources:
            sources.append(chunk["source"])

    return QueryResponse(answer=answer, sources=sources)






# from backend.app.schemas.query import QueryRequest, QueryResponse


# from backend.app.services.retrieval import retrieve_chunks
# from backend.app.services.generation import generate_answer

# router = APIRouter()


# @router.post("/query", response_model=QueryResponse)
# def query_dreamscape(request: QueryRequest):
#     """
#     Receive a question, retrieve relevant Dreamscape information,
#     and generate a grounded answer.
#     """

#     # Step 1: Retrieve relevant chunks
#     retrieved_chunks = retrieve_chunks(request.question)

#     # Step 2: Generate grounded answer
#     answer = generate_answer(
#         request.question,
#         retrieved_chunks
#     )

#     # Step 3: Collect source filenames
#     sources = []

#     for chunk in retrieved_chunks:
#         if chunk["source"] not in sources:
#             sources.append(chunk["source"])

#     return QueryResponse(
#         answer=answer,
#         sources=sources
#     )