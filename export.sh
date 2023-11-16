#!/usr/bin/env bash

./build.sh

docker save joeranbosma/dragon_baseline_roberta_large_multilingual:latest | gzip -c > dragon_baseline_roberta_large_multilingual.tar.gz
