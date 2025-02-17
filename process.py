from dragon_baseline import DragonBaseline


class DragonRobertaLargeGeneralDomain(DragonBaseline):
    def __init__(self, **kwargs):
        """
        Adapt the DRAGON baseline to use the xlm-roberta-large model.
        Note: when manually changing the model, update the Dockerfile to pre-download that model.
        """
        super().__init__(**kwargs)
        self.model_name = "xlm-roberta-large"
        self.per_device_train_batch_size = 1
        self.gradient_accumulation_steps = 8
        self.gradient_checkpointing = False
        self.max_seq_length = 512
        self.learning_rate = 1e-05
        self.num_train_epochs = 5
        self.create_strided_training_examples = False


if __name__ == "__main__":
    DragonRobertaLargeGeneralDomain().process()
