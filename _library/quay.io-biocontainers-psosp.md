---
layout: container
name:  "quay.io/biocontainers/psosp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/psosp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/psosp/container.yaml"
updated_at: "2026-01-25 03:59:39.614422"
latest: "1.1.2--pyhdfd78af_2"
container_url: "https://biocontainers.pro/tools/psosp"
aliases:
 - "bed2fasta"
 - "centrimo-plots"
 - "checkv"
 - "derangement"
 - "dtc"
 - "fasta-file-indexer"
 - "fasta-holdout-set"
 - "fasta-re-match"
 - "meme-chip_html_to_tsv"
 - "momo"
 - "prodigal-gv"
 - "prosite2meme"
 - "psosp"
 - "sea"
 - "simplepp"
 - "streme"
 - "streme_xml_to_html"
 - "tgene"
 - "tts"
 - "xstreme"
 - "xstreme_html_to_tsv"
 - "corepack"
 - "alphtype"
 - "ama"
 - "ama-qvalues"
 - "ame"
 - "beeml2meme"
 - "centrimo"
 - "ceqlogo"
 - "chen2meme"
 - "clustalw2fasta"
 - "clustalw2phylip"
 - "compute-prior-dist"
 - "compute-uniform-priors"
 - "create-priors"
 - "dreme"
 - "dreme_xml_to_html"
 - "dreme_xml_to_txt"
 - "dust"
 - "elm2meme"
 - "fasta-center"
 - "fasta-dinucleotide-shuffle"
 - "fasta-fetch"
 - "fasta-get-markov"
 - "fasta-grep"
 - "fasta-hamming-enrich"
versions:
 - "1.1.1--pyhdfd78af_0"
 - "1.1.2--pyhdfd78af_0"
 - "1.1.2--pyhdfd78af_2"
description: "singularity registry hpc automated addition for psosp"
config: {"url": "https://biocontainers.pro/tools/psosp", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for psosp", "latest": {"1.1.2--pyhdfd78af_2": "sha256:12e50a529213262109bcd1b99e6a85b7ec28b77f61b5082c6859e00b55b7e9f4"}, "tags": {"1.1.1--pyhdfd78af_0": "sha256:1b2eb4a7ec891811c5d384adfb79a4d784ad4c10cab54d84690c2c1a6a9f5839", "1.1.2--pyhdfd78af_0": "sha256:d28761f3eb49eae281dcf55103ae4b1906e0e59461dc60fe87a4d84af884d395", "1.1.2--pyhdfd78af_2": "sha256:12e50a529213262109bcd1b99e6a85b7ec28b77f61b5082c6859e00b55b7e9f4"}, "docker": "quay.io/biocontainers/psosp", "aliases": {"bed2fasta": "/usr/local/bin/bed2fasta", "centrimo-plots": "/usr/local/bin/centrimo-plots", "checkv": "/usr/local/bin/checkv", "derangement": "/usr/local/bin/derangement", "dtc": "/usr/local/bin/dtc", "fasta-file-indexer": "/usr/local/bin/fasta-file-indexer", "fasta-holdout-set": "/usr/local/bin/fasta-holdout-set", "fasta-re-match": "/usr/local/bin/fasta-re-match", "meme-chip_html_to_tsv": "/usr/local/bin/meme-chip_html_to_tsv", "momo": "/usr/local/bin/momo", "prodigal-gv": "/usr/local/bin/prodigal-gv", "prosite2meme": "/usr/local/bin/prosite2meme", "psosp": "/usr/local/bin/psosp", "sea": "/usr/local/bin/sea", "simplepp": "/usr/local/bin/simplepp", "streme": "/usr/local/bin/streme", "streme_xml_to_html": "/usr/local/bin/streme_xml_to_html", "tgene": "/usr/local/bin/tgene", "tts": "/usr/local/bin/tts", "xstreme": "/usr/local/bin/xstreme", "xstreme_html_to_tsv": "/usr/local/bin/xstreme_html_to_tsv", "corepack": "/usr/local/bin/corepack", "alphtype": "/usr/local/bin/alphtype", "ama": "/usr/local/bin/ama", "ama-qvalues": "/usr/local/bin/ama-qvalues", "ame": "/usr/local/bin/ame", "beeml2meme": "/usr/local/bin/beeml2meme", "centrimo": "/usr/local/bin/centrimo", "ceqlogo": "/usr/local/bin/ceqlogo", "chen2meme": "/usr/local/bin/chen2meme", "clustalw2fasta": "/usr/local/bin/clustalw2fasta", "clustalw2phylip": "/usr/local/bin/clustalw2phylip", "compute-prior-dist": "/usr/local/bin/compute-prior-dist", "compute-uniform-priors": "/usr/local/bin/compute-uniform-priors", "create-priors": "/usr/local/bin/create-priors", "dreme": "/usr/local/bin/dreme", "dreme_xml_to_html": "/usr/local/bin/dreme_xml_to_html", "dreme_xml_to_txt": "/usr/local/bin/dreme_xml_to_txt", "dust": "/usr/local/bin/dust", "elm2meme": "/usr/local/bin/elm2meme", "fasta-center": "/usr/local/bin/fasta-center", "fasta-dinucleotide-shuffle": "/usr/local/bin/fasta-dinucleotide-shuffle", "fasta-fetch": "/usr/local/bin/fasta-fetch", "fasta-get-markov": "/usr/local/bin/fasta-get-markov", "fasta-grep": "/usr/local/bin/fasta-grep", "fasta-hamming-enrich": "/usr/local/bin/fasta-hamming-enrich"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/psosp.
singularity registry hpc automated addition for psosp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/psosp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/psosp:1.1.2--pyhdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/psosp/1.1.2--pyhdfd78af_2
$ module help quay.io/biocontainers/psosp/1.1.2--pyhdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### psosp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### psosp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### psosp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### psosp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### psosp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### psosp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bed2fasta

```bash
$ singularity exec <container> /usr/local/bin/bed2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/bed2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrimo-plots

```bash
$ singularity exec <container> /usr/local/bin/centrimo-plots
$ podman run --it --rm --entrypoint /usr/local/bin/centrimo-plots   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrimo-plots   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checkv

```bash
$ singularity exec <container> /usr/local/bin/checkv
$ podman run --it --rm --entrypoint /usr/local/bin/checkv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checkv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### derangement

```bash
$ singularity exec <container> /usr/local/bin/derangement
$ podman run --it --rm --entrypoint /usr/local/bin/derangement   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/derangement   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dtc

```bash
$ singularity exec <container> /usr/local/bin/dtc
$ podman run --it --rm --entrypoint /usr/local/bin/dtc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dtc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-file-indexer

```bash
$ singularity exec <container> /usr/local/bin/fasta-file-indexer
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-file-indexer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-file-indexer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-holdout-set

```bash
$ singularity exec <container> /usr/local/bin/fasta-holdout-set
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-holdout-set   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-holdout-set   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-re-match

```bash
$ singularity exec <container> /usr/local/bin/fasta-re-match
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-re-match   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-re-match   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meme-chip_html_to_tsv

```bash
$ singularity exec <container> /usr/local/bin/meme-chip_html_to_tsv
$ podman run --it --rm --entrypoint /usr/local/bin/meme-chip_html_to_tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meme-chip_html_to_tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### momo

```bash
$ singularity exec <container> /usr/local/bin/momo
$ podman run --it --rm --entrypoint /usr/local/bin/momo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/momo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prodigal-gv

```bash
$ singularity exec <container> /usr/local/bin/prodigal-gv
$ podman run --it --rm --entrypoint /usr/local/bin/prodigal-gv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prodigal-gv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prosite2meme

```bash
$ singularity exec <container> /usr/local/bin/prosite2meme
$ podman run --it --rm --entrypoint /usr/local/bin/prosite2meme   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prosite2meme   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psosp

```bash
$ singularity exec <container> /usr/local/bin/psosp
$ podman run --it --rm --entrypoint /usr/local/bin/psosp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psosp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sea

```bash
$ singularity exec <container> /usr/local/bin/sea
$ podman run --it --rm --entrypoint /usr/local/bin/sea   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sea   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### simplepp

```bash
$ singularity exec <container> /usr/local/bin/simplepp
$ podman run --it --rm --entrypoint /usr/local/bin/simplepp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/simplepp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streme

```bash
$ singularity exec <container> /usr/local/bin/streme
$ podman run --it --rm --entrypoint /usr/local/bin/streme   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streme   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streme_xml_to_html

```bash
$ singularity exec <container> /usr/local/bin/streme_xml_to_html
$ podman run --it --rm --entrypoint /usr/local/bin/streme_xml_to_html   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streme_xml_to_html   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tgene

```bash
$ singularity exec <container> /usr/local/bin/tgene
$ podman run --it --rm --entrypoint /usr/local/bin/tgene   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tgene   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tts

```bash
$ singularity exec <container> /usr/local/bin/tts
$ podman run --it --rm --entrypoint /usr/local/bin/tts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xstreme

```bash
$ singularity exec <container> /usr/local/bin/xstreme
$ podman run --it --rm --entrypoint /usr/local/bin/xstreme   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xstreme   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xstreme_html_to_tsv

```bash
$ singularity exec <container> /usr/local/bin/xstreme_html_to_tsv
$ podman run --it --rm --entrypoint /usr/local/bin/xstreme_html_to_tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xstreme_html_to_tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### corepack

```bash
$ singularity exec <container> /usr/local/bin/corepack
$ podman run --it --rm --entrypoint /usr/local/bin/corepack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/corepack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alphtype

```bash
$ singularity exec <container> /usr/local/bin/alphtype
$ podman run --it --rm --entrypoint /usr/local/bin/alphtype   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alphtype   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ama

```bash
$ singularity exec <container> /usr/local/bin/ama
$ podman run --it --rm --entrypoint /usr/local/bin/ama   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ama   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ama-qvalues

```bash
$ singularity exec <container> /usr/local/bin/ama-qvalues
$ podman run --it --rm --entrypoint /usr/local/bin/ama-qvalues   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ama-qvalues   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ame

```bash
$ singularity exec <container> /usr/local/bin/ame
$ podman run --it --rm --entrypoint /usr/local/bin/ame   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ame   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### beeml2meme

```bash
$ singularity exec <container> /usr/local/bin/beeml2meme
$ podman run --it --rm --entrypoint /usr/local/bin/beeml2meme   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/beeml2meme   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### centrimo

```bash
$ singularity exec <container> /usr/local/bin/centrimo
$ podman run --it --rm --entrypoint /usr/local/bin/centrimo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/centrimo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ceqlogo

```bash
$ singularity exec <container> /usr/local/bin/ceqlogo
$ podman run --it --rm --entrypoint /usr/local/bin/ceqlogo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ceqlogo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chen2meme

```bash
$ singularity exec <container> /usr/local/bin/chen2meme
$ podman run --it --rm --entrypoint /usr/local/bin/chen2meme   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chen2meme   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clustalw2fasta

```bash
$ singularity exec <container> /usr/local/bin/clustalw2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/clustalw2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clustalw2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clustalw2phylip

```bash
$ singularity exec <container> /usr/local/bin/clustalw2phylip
$ podman run --it --rm --entrypoint /usr/local/bin/clustalw2phylip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clustalw2phylip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compute-prior-dist

```bash
$ singularity exec <container> /usr/local/bin/compute-prior-dist
$ podman run --it --rm --entrypoint /usr/local/bin/compute-prior-dist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compute-prior-dist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compute-uniform-priors

```bash
$ singularity exec <container> /usr/local/bin/compute-uniform-priors
$ podman run --it --rm --entrypoint /usr/local/bin/compute-uniform-priors   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compute-uniform-priors   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create-priors

```bash
$ singularity exec <container> /usr/local/bin/create-priors
$ podman run --it --rm --entrypoint /usr/local/bin/create-priors   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create-priors   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dreme

```bash
$ singularity exec <container> /usr/local/bin/dreme
$ podman run --it --rm --entrypoint /usr/local/bin/dreme   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dreme   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dreme_xml_to_html

```bash
$ singularity exec <container> /usr/local/bin/dreme_xml_to_html
$ podman run --it --rm --entrypoint /usr/local/bin/dreme_xml_to_html   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dreme_xml_to_html   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dreme_xml_to_txt

```bash
$ singularity exec <container> /usr/local/bin/dreme_xml_to_txt
$ podman run --it --rm --entrypoint /usr/local/bin/dreme_xml_to_txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dreme_xml_to_txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dust

```bash
$ singularity exec <container> /usr/local/bin/dust
$ podman run --it --rm --entrypoint /usr/local/bin/dust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elm2meme

```bash
$ singularity exec <container> /usr/local/bin/elm2meme
$ podman run --it --rm --entrypoint /usr/local/bin/elm2meme   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elm2meme   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-center

```bash
$ singularity exec <container> /usr/local/bin/fasta-center
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-center   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-center   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-dinucleotide-shuffle

```bash
$ singularity exec <container> /usr/local/bin/fasta-dinucleotide-shuffle
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-dinucleotide-shuffle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-dinucleotide-shuffle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-fetch

```bash
$ singularity exec <container> /usr/local/bin/fasta-fetch
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-fetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-fetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-get-markov

```bash
$ singularity exec <container> /usr/local/bin/fasta-get-markov
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-get-markov   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-get-markov   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-grep

```bash
$ singularity exec <container> /usr/local/bin/fasta-grep
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-grep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-grep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-hamming-enrich

```bash
$ singularity exec <container> /usr/local/bin/fasta-hamming-enrich
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-hamming-enrich   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-hamming-enrich   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)