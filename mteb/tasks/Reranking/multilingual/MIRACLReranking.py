from __future__ import annotations

import logging
from typing import Any

from datasets import Dataset

from mteb.abstasks.MultilingualTask import MultilingualTask
from mteb.abstasks.TaskMetadata import TaskMetadata
from mteb.encoder_interface import Encoder
from mteb.evaluation.evaluators import RerankingEvaluator
from mteb.load_results.task_results import ScoresDict

from ....abstasks.AbsTaskReranking import AbsTaskReranking

logger = logging.getLogger(__name__)

_EVAL_SPLIT = "dev"
_LANGUAGES = {
    "ar": ["ara-Arab"],
    "bn": ["ben-Beng"],
    "de": ["deu-Latn"],
    "en": ["eng-Latn"],
    "es": ["spa-Latn"],
    "fa": ["fas-Arab"],
    "fi": ["fin-Latn"],
    "fr": ["fra-Latn"],
    "hi": ["hin-Deva"],
    "id": ["ind-Latn"],
    "ja": ["jpn-Jpan"],
    "ko": ["kor-Kore"],
    "ru": ["rus-Cyrl"],
    "sw": ["swa-Latn"],
    "te": ["tel-Telu"],
    "th": ["tha-Thai"],
    "yo": ["yor-Latn"],
    "zh": ["zho-Hans"],
}

_CITATION = r"""@article{10.1162/tacl_a_00595,
  author = {Zhang, Xinyu and Thakur, Nandan and Ogundepo, Odunayo and Kamalloo, Ehsan and Alfonso-Hermelo, David and Li, Xiaoguang and Liu, Qun and Rezagholizadeh, Mehdi and Lin, Jimmy},
  doi = {10.1162/tacl_a_00595},
  issn = {2307-387X},
  journal = {Transactions of the Association for Computational Linguistics},
  month = {09},
  pages = {1114-1131},
  title = {{MIRACL: A Multilingual Retrieval Dataset Covering 18 Diverse Languages}},
  volume = {11},
  year = {2023},
}"""


class MIRACLReranking(MultilingualTask, AbsTaskReranking):
    metadata = TaskMetadata(
        name="MIRACLReranking",
        description="MIRACL (Multilingual Information Retrieval Across a Continuum of Languages) is a multilingual retrieval dataset that focuses on search across 18 different languages.",
        reference="https://project-miracl.github.io/",
        dataset={
            "path": "miracl/mmteb-miracl-reranking",
            "revision": "6d1962c527217f8927fca80f890f14f36b2802af",
            "trust_remote_code": True,
        },
        type="Reranking",
        category="s2s",
        modalities=["text"],
        eval_splits=[_EVAL_SPLIT],
        eval_langs=_LANGUAGES,
        main_score="NDCG@10(MIRACL)",
        date=("2022-06-01", "2023-01-30"),
        domains=["Encyclopaedic", "Written"],
        task_subtypes=[],
        license="cc-by-sa-4.0",
        annotations_creators="expert-annotated",
        dialect=[],
        sample_creation="created",
        bibtex_citation=_CITATION,
        prompt={
            "query": "Given a question, retrieve Wikipedia passages that answer the question"
        },
        adapted_from=["MIRACLRetrieval"],
    )

    def _evaluate_subset(
        self,
        model: Encoder,
        data_split: Dataset,
        *,
        encode_kwargs: dict[str, Any] = {},
        **kwargs: Any,
    ) -> ScoresDict:
        evaluator = RerankingEvaluator(
            samples=data_split,
            evaluator_type="miracl",
            task_name=self.metadata.name,
            encode_kwargs=encode_kwargs,
            **kwargs,
        )
        scores = evaluator(model)

        self._add_main_score(scores)
        return scores
