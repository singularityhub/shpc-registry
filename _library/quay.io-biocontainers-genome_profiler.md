---
layout: container
name:  "quay.io/biocontainers/genome_profiler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genome_profiler/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/genome_profiler/container.yaml"
updated_at: "2025-12-13 03:35:38.066795"
latest: "0.4.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/genome_profiler"
aliases:
 - "RNAconsensus"
 - "bio"
 - "constants.py"
 - "dataformat"
 - "datasets"
 - "ectyper"
 - "ectyper_init"
 - "fasta_filter.py"
 - "genome_profiler"
 - "integron_finder"
 - "integron_merge"
 - "integron_split"
 - "isPredict.py"
 - "is_analysis.py"
 - "isescan.py"
 - "pred.py"
 - "pyssw.py"
 - "ssw_wrap.py"
 - "tools.py"
 - "abricate"
 - "abricate-get_db"
 - "asn1Coding"
 - "asn1Decoding"
 - "asn1Parser"
 - "p11-kit"
 - "p11tool"
 - "trust"
 - "FragGeneScan"
 - "run_FragGeneScan.pl"
 - "dotenv"
 - "gawk-5.3.1"
 - "any2fasta"
 - "TMalign"
 - "make_pscores.pl"
 - "funzip"
 - "httpx"
 - "poa"
 - "unzipsfx"
 - "zipgrep"
 - "zipinfo"
 - "unzip"
 - "RNAmultifold"
 - "clustalo"
 - "certtool"
versions:
 - "0.4.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for genome_profiler"
config: {"url": "https://biocontainers.pro/tools/genome_profiler", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for genome_profiler", "latest": {"0.4.2--pyhdfd78af_0": "sha256:70d6ab215f48325a8de8fc1f8ad0b2206d3fc92357f061fe348b16dab90d2285"}, "tags": {"0.4.2--pyhdfd78af_0": "sha256:70d6ab215f48325a8de8fc1f8ad0b2206d3fc92357f061fe348b16dab90d2285"}, "docker": "quay.io/biocontainers/genome_profiler", "aliases": {"RNAconsensus": "/usr/local/bin/RNAconsensus", "bio": "/usr/local/bin/bio", "constants.py": "/usr/local/bin/constants.py", "dataformat": "/usr/local/bin/dataformat", "datasets": "/usr/local/bin/datasets", "ectyper": "/usr/local/bin/ectyper", "ectyper_init": "/usr/local/bin/ectyper_init", "fasta_filter.py": "/usr/local/bin/fasta_filter.py", "genome_profiler": "/usr/local/bin/genome_profiler", "integron_finder": "/usr/local/bin/integron_finder", "integron_merge": "/usr/local/bin/integron_merge", "integron_split": "/usr/local/bin/integron_split", "isPredict.py": "/usr/local/bin/isPredict.py", "is_analysis.py": "/usr/local/bin/is_analysis.py", "isescan.py": "/usr/local/bin/isescan.py", "pred.py": "/usr/local/bin/pred.py", "pyssw.py": "/usr/local/bin/pyssw.py", "ssw_wrap.py": "/usr/local/bin/ssw_wrap.py", "tools.py": "/usr/local/bin/tools.py", "abricate": "/usr/local/bin/abricate", "abricate-get_db": "/usr/local/bin/abricate-get_db", "asn1Coding": "/usr/local/bin/asn1Coding", "asn1Decoding": "/usr/local/bin/asn1Decoding", "asn1Parser": "/usr/local/bin/asn1Parser", "p11-kit": "/usr/local/bin/p11-kit", "p11tool": "/usr/local/bin/p11tool", "trust": "/usr/local/bin/trust", "FragGeneScan": "/usr/local/bin/FragGeneScan", "run_FragGeneScan.pl": "/usr/local/bin/run_FragGeneScan.pl", "dotenv": "/usr/local/bin/dotenv", "gawk-5.3.1": "/usr/local/bin/gawk-5.3.1", "any2fasta": "/usr/local/bin/any2fasta", "TMalign": "/usr/local/bin/TMalign", "make_pscores.pl": "/usr/local/bin/make_pscores.pl", "funzip": "/usr/local/bin/funzip", "httpx": "/usr/local/bin/httpx", "poa": "/usr/local/bin/poa", "unzipsfx": "/usr/local/bin/unzipsfx", "zipgrep": "/usr/local/bin/zipgrep", "zipinfo": "/usr/local/bin/zipinfo", "unzip": "/usr/local/bin/unzip", "RNAmultifold": "/usr/local/bin/RNAmultifold", "clustalo": "/usr/local/bin/clustalo", "certtool": "/usr/local/bin/certtool"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genome_profiler.
singularity registry hpc automated addition for genome_profiler
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genome_profiler
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genome_profiler:0.4.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genome_profiler/0.4.2--pyhdfd78af_0
$ module help quay.io/biocontainers/genome_profiler/0.4.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genome_profiler-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genome_profiler-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genome_profiler-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genome_profiler-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genome_profiler-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genome_profiler-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RNAconsensus

```bash
$ singularity exec <container> /usr/local/bin/RNAconsensus
$ podman run --it --rm --entrypoint /usr/local/bin/RNAconsensus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAconsensus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bio

```bash
$ singularity exec <container> /usr/local/bin/bio
$ podman run --it --rm --entrypoint /usr/local/bin/bio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### constants.py

```bash
$ singularity exec <container> /usr/local/bin/constants.py
$ podman run --it --rm --entrypoint /usr/local/bin/constants.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/constants.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dataformat

```bash
$ singularity exec <container> /usr/local/bin/dataformat
$ podman run --it --rm --entrypoint /usr/local/bin/dataformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dataformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### datasets

```bash
$ singularity exec <container> /usr/local/bin/datasets
$ podman run --it --rm --entrypoint /usr/local/bin/datasets   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/datasets   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ectyper

```bash
$ singularity exec <container> /usr/local/bin/ectyper
$ podman run --it --rm --entrypoint /usr/local/bin/ectyper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ectyper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ectyper_init

```bash
$ singularity exec <container> /usr/local/bin/ectyper_init
$ podman run --it --rm --entrypoint /usr/local/bin/ectyper_init   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ectyper_init   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_filter.py

```bash
$ singularity exec <container> /usr/local/bin/fasta_filter.py
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_filter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genome_profiler

```bash
$ singularity exec <container> /usr/local/bin/genome_profiler
$ podman run --it --rm --entrypoint /usr/local/bin/genome_profiler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genome_profiler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### integron_finder

```bash
$ singularity exec <container> /usr/local/bin/integron_finder
$ podman run --it --rm --entrypoint /usr/local/bin/integron_finder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/integron_finder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### integron_merge

```bash
$ singularity exec <container> /usr/local/bin/integron_merge
$ podman run --it --rm --entrypoint /usr/local/bin/integron_merge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/integron_merge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### integron_split

```bash
$ singularity exec <container> /usr/local/bin/integron_split
$ podman run --it --rm --entrypoint /usr/local/bin/integron_split   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/integron_split   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isPredict.py

```bash
$ singularity exec <container> /usr/local/bin/isPredict.py
$ podman run --it --rm --entrypoint /usr/local/bin/isPredict.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isPredict.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### is_analysis.py

```bash
$ singularity exec <container> /usr/local/bin/is_analysis.py
$ podman run --it --rm --entrypoint /usr/local/bin/is_analysis.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/is_analysis.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isescan.py

```bash
$ singularity exec <container> /usr/local/bin/isescan.py
$ podman run --it --rm --entrypoint /usr/local/bin/isescan.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isescan.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pred.py

```bash
$ singularity exec <container> /usr/local/bin/pred.py
$ podman run --it --rm --entrypoint /usr/local/bin/pred.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pred.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyssw.py

```bash
$ singularity exec <container> /usr/local/bin/pyssw.py
$ podman run --it --rm --entrypoint /usr/local/bin/pyssw.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyssw.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ssw_wrap.py

```bash
$ singularity exec <container> /usr/local/bin/ssw_wrap.py
$ podman run --it --rm --entrypoint /usr/local/bin/ssw_wrap.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ssw_wrap.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tools.py

```bash
$ singularity exec <container> /usr/local/bin/tools.py
$ podman run --it --rm --entrypoint /usr/local/bin/tools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tools.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abricate

```bash
$ singularity exec <container> /usr/local/bin/abricate
$ podman run --it --rm --entrypoint /usr/local/bin/abricate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abricate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abricate-get_db

```bash
$ singularity exec <container> /usr/local/bin/abricate-get_db
$ podman run --it --rm --entrypoint /usr/local/bin/abricate-get_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abricate-get_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asn1Coding

```bash
$ singularity exec <container> /usr/local/bin/asn1Coding
$ podman run --it --rm --entrypoint /usr/local/bin/asn1Coding   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asn1Coding   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asn1Decoding

```bash
$ singularity exec <container> /usr/local/bin/asn1Decoding
$ podman run --it --rm --entrypoint /usr/local/bin/asn1Decoding   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asn1Decoding   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asn1Parser

```bash
$ singularity exec <container> /usr/local/bin/asn1Parser
$ podman run --it --rm --entrypoint /usr/local/bin/asn1Parser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asn1Parser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### p11-kit

```bash
$ singularity exec <container> /usr/local/bin/p11-kit
$ podman run --it --rm --entrypoint /usr/local/bin/p11-kit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/p11-kit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### p11tool

```bash
$ singularity exec <container> /usr/local/bin/p11tool
$ podman run --it --rm --entrypoint /usr/local/bin/p11tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/p11tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trust

```bash
$ singularity exec <container> /usr/local/bin/trust
$ podman run --it --rm --entrypoint /usr/local/bin/trust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FragGeneScan

```bash
$ singularity exec <container> /usr/local/bin/FragGeneScan
$ podman run --it --rm --entrypoint /usr/local/bin/FragGeneScan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FragGeneScan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_FragGeneScan.pl

```bash
$ singularity exec <container> /usr/local/bin/run_FragGeneScan.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run_FragGeneScan.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_FragGeneScan.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dotenv

```bash
$ singularity exec <container> /usr/local/bin/dotenv
$ podman run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.3.1

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.3.1
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### any2fasta

```bash
$ singularity exec <container> /usr/local/bin/any2fasta
$ podman run --it --rm --entrypoint /usr/local/bin/any2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/any2fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TMalign

```bash
$ singularity exec <container> /usr/local/bin/TMalign
$ podman run --it --rm --entrypoint /usr/local/bin/TMalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TMalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_pscores.pl

```bash
$ singularity exec <container> /usr/local/bin/make_pscores.pl
$ podman run --it --rm --entrypoint /usr/local/bin/make_pscores.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_pscores.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### funzip

```bash
$ singularity exec <container> /usr/local/bin/funzip
$ podman run --it --rm --entrypoint /usr/local/bin/funzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/funzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### httpx

```bash
$ singularity exec <container> /usr/local/bin/httpx
$ podman run --it --rm --entrypoint /usr/local/bin/httpx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/httpx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### poa

```bash
$ singularity exec <container> /usr/local/bin/poa
$ podman run --it --rm --entrypoint /usr/local/bin/poa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/poa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unzipsfx

```bash
$ singularity exec <container> /usr/local/bin/unzipsfx
$ podman run --it --rm --entrypoint /usr/local/bin/unzipsfx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unzipsfx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipgrep

```bash
$ singularity exec <container> /usr/local/bin/zipgrep
$ podman run --it --rm --entrypoint /usr/local/bin/zipgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipinfo

```bash
$ singularity exec <container> /usr/local/bin/zipinfo
$ podman run --it --rm --entrypoint /usr/local/bin/zipinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unzip

```bash
$ singularity exec <container> /usr/local/bin/unzip
$ podman run --it --rm --entrypoint /usr/local/bin/unzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RNAmultifold

```bash
$ singularity exec <container> /usr/local/bin/RNAmultifold
$ podman run --it --rm --entrypoint /usr/local/bin/RNAmultifold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RNAmultifold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clustalo

```bash
$ singularity exec <container> /usr/local/bin/clustalo
$ podman run --it --rm --entrypoint /usr/local/bin/clustalo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clustalo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### certtool

```bash
$ singularity exec <container> /usr/local/bin/certtool
$ podman run --it --rm --entrypoint /usr/local/bin/certtool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/certtool   -v ${PWD} -w ${PWD} <container> -c " $@"
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