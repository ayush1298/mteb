from __future__ import annotations

from mteb.abstasks.AbsTaskClassification import AbsTaskClassification
from mteb.abstasks.TaskMetadata import TaskMetadata


class RestaurantReviewSentimentClassification(AbsTaskClassification):
    metadata = TaskMetadata(
        name="RestaurantReviewSentimentClassification",
        dataset={
            "path": "hadyelsahar/ar_res_reviews",
            "revision": "d51bf2435d030e0041344f576c5e8d7154828977",
        },
        description="Dataset of 8364 restaurant reviews from qaym.com in Arabic for sentiment analysis",
        reference="https://link.springer.com/chapter/10.1007/978-3-319-18117-2_2",
        type="Classification",
        category="s2s",
        modalities=["text"],
        eval_splits=["train"],
        eval_langs=["ara-Arab"],
        main_score="accuracy",
        date=("2014-01-01", "2015-01-01"),
        domains=["Reviews", "Written"],
        task_subtypes=["Sentiment/Hate speech"],
        license="not specified",
        annotations_creators="derived",
        dialect=["ara-arab-EG", "ara-arab-JO", "ara-arab-SA"],
        sample_creation="found",
        bibtex_citation=r"""
@inproceedings{elsahar2015building,
  author = {ElSahar, Hady and El-Beltagy, Samhaa R},
  booktitle = {International conference on intelligent text processing and computational linguistics},
  organization = {Springer},
  pages = {23--34},
  title = {Building large arabic multi-domain resources for sentiment analysis},
  year = {2015},
}
""",
    )

    def dataset_transform(self):
        # labels: 0 negative, 1 positive
        self.dataset = self.dataset.rename_column("polarity", "label")
        self.dataset = self.stratified_subsampling(
            self.dataset, seed=self.seed, splits=["train"]
        )
