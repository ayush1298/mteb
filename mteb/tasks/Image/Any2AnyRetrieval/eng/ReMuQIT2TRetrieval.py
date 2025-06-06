from __future__ import annotations

from mteb.abstasks.Image.AbsTaskAny2AnyRetrieval import AbsTaskAny2AnyRetrieval
from mteb.abstasks.TaskMetadata import TaskMetadata


class ReMuQIT2TRetrieval(AbsTaskAny2AnyRetrieval):
    metadata = TaskMetadata(
        name="ReMuQIT2TRetrieval",
        description="Retrieval of a Wiki passage to answer a query about an image.",
        reference="https://github.com/luomancs/ReMuQ",
        dataset={
            "path": "izhx/UMRB-ReMuQ",
            "revision": "f0bd5955d2897bd1bed56546e88082d966c90a80",
        },
        type="Any2AnyRetrieval",
        category="it2t",
        eval_splits=["test"],
        eval_langs=["eng-Latn"],
        main_score="cv_recall_at_5",
        date=("2023-05-15", "2023-07-09"),
        domains=["Encyclopaedic"],
        task_subtypes=["Image Text Retrieval"],
        license="cc0-1.0",
        annotations_creators="derived",
        dialect=[],
        modalities=["image", "text"],
        sample_creation="created",
        bibtex_citation=r"""
@inproceedings{luo-etal-2023-end,
  address = {Toronto, Canada},
  author = {Luo, Man  and
Fang, Zhiyuan  and
Gokhale, Tejas  and
Yang, Yezhou  and
Baral, Chitta},
  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  doi = {10.18653/v1/2023.acl-long.478},
  editor = {Rogers, Anna  and
Boyd-Graber, Jordan  and
Okazaki, Naoaki},
  month = jul,
  pages = {8573--8589},
  publisher = {Association for Computational Linguistics},
  title = {End-to-end Knowledge Retrieval with Multi-modal Queries},
  url = {https://aclanthology.org/2023.acl-long.478},
  year = {2023},
}
""",
        prompt={
            "query": "Retrieve a fact-based paragraph that provides an answer to the given query about the image."
        },
        descriptive_stats={
            "n_samples": {"test": 3609},
            "avg_character_length": {
                "test": {
                    "average_document_length": 208.18675158868538,
                    "average_query_length": 73.85508451094486,
                    "num_documents": 138794,
                    "num_queries": 3609,
                    "average_relevant_docs_per_query": 1.0,
                }
            },
        },
    )
