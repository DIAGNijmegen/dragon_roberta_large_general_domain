#!/usr/bin/env bash

./build.sh

docker save joeranbosma/dragon_roberta_large_general_domain:latest | gzip -c > dragon_roberta_large_general_domain.tar.gz
