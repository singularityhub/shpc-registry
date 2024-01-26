---
layout: container
name:  "quay.io/biocontainers/lotus2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lotus2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lotus2/container.yaml"
updated_at: "2024-01-26 03:05:25.020577"
latest: "2.31--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/lotus2"
aliases:
 - "ITSx"
 - "LCA"
 - "amplicon_contingency_table.py"
 - "graph_plot.py"
 - "iqtree2"
 - "lambda"
 - "lambda_indexer"
 - "lotus2"
 - "rdp_classifier"
 - "rtk"
 - "sdm"
 - "swarm"
 - "clustalo"
 - "zip"
 - "iqtree"
 - "funzip"
 - "unzipsfx"
 - "zipgrep"
 - "zipinfo"
 - "igraph"
 - "vsearch"
 - "FET.pl"
versions:
 - "2.21--hdfd78af_0"
 - "2.22--hdfd78af_0"
 - "2.23--hdfd78af_0"
 - "2.24--hdfd78af_0"
 - "2.25--hdfd78af_0"
 - "2.28--hdfd78af_0"
 - "2.28.1--hdfd78af_1"
 - "2.30--hdfd78af_1"
 - "2.31--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for lotus2"
config: {"url": "https://biocontainers.pro/tools/lotus2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for lotus2", "latest": {"2.31--hdfd78af_0": "sha256:94d6d40e4dd4e4974b6231e377a982a1709a91defe6f802526e5924e1773bb1a"}, "tags": {"2.21--hdfd78af_0": "sha256:bbcf2903a884af263aba5f55020c29dcb68749fa51873d59d0959737a6400f4d", "2.22--hdfd78af_0": "sha256:9c3a69446d09c28cbbe9b5e2c8e68ace1c2f57034e5c3393a18464d2c5b6f3a0", "2.23--hdfd78af_0": "sha256:08f16d23a51b827b58a676c355ae5fa0a8c5eb6a014323adb99d458cb3684e21", "2.24--hdfd78af_0": "sha256:42874836caa74c58affe44be9c8f033f9df8a3d46308c6eaf8a2397fd9802e69", "2.25--hdfd78af_0": "sha256:fedc4368bc3e3017594398f9541486134438a51171df690d006ba4cee24e6171", "2.28--hdfd78af_0": "sha256:a6f76aca81728a9042cdddfc4b50a00bf26bcff47f7208d5f1e13bf3bb36b496", "2.28.1--hdfd78af_1": "sha256:6e25bf7c05341858dc68ae1b8908a62dd18d46baf5208054baee2dcbfbdca6a0", "2.30--hdfd78af_1": "sha256:02a51c7d81af45937d3066bb69afda3528e80d124b0c87eab1ee1296179ee74f", "2.31--hdfd78af_0": "sha256:94d6d40e4dd4e4974b6231e377a982a1709a91defe6f802526e5924e1773bb1a"}, "docker": "quay.io/biocontainers/lotus2", "aliases": {"ITSx": "/usr/local/bin/ITSx", "LCA": "/usr/local/bin/LCA", "amplicon_contingency_table.py": "/usr/local/bin/amplicon_contingency_table.py", "graph_plot.py": "/usr/local/bin/graph_plot.py", "iqtree2": "/usr/local/bin/iqtree2", "lambda": "/usr/local/bin/lambda", "lambda_indexer": "/usr/local/bin/lambda_indexer", "lotus2": "/usr/local/bin/lotus2", "rdp_classifier": "/usr/local/bin/rdp_classifier", "rtk": "/usr/local/bin/rtk", "sdm": "/usr/local/bin/sdm", "swarm": "/usr/local/bin/swarm", "clustalo": "/usr/local/bin/clustalo", "zip": "/usr/local/bin/zip", "iqtree": "/usr/local/bin/iqtree", "funzip": "/usr/local/bin/funzip", "unzipsfx": "/usr/local/bin/unzipsfx", "zipgrep": "/usr/local/bin/zipgrep", "zipinfo": "/usr/local/bin/zipinfo", "igraph": "/usr/local/bin/igraph", "vsearch": "/usr/local/bin/vsearch", "FET.pl": "/usr/local/bin/FET.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lotus2.
shpc-registry automated BioContainers addition for lotus2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lotus2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lotus2:2.31--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lotus2/2.31--hdfd78af_0
$ module help quay.io/biocontainers/lotus2/2.31--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lotus2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lotus2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lotus2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lotus2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lotus2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lotus2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ITSx

```bash
$ singularity exec <container> /usr/local/bin/ITSx
$ podman run --it --rm --entrypoint /usr/local/bin/ITSx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ITSx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LCA

```bash
$ singularity exec <container> /usr/local/bin/LCA
$ podman run --it --rm --entrypoint /usr/local/bin/LCA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LCA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### amplicon_contingency_table.py

```bash
$ singularity exec <container> /usr/local/bin/amplicon_contingency_table.py
$ podman run --it --rm --entrypoint /usr/local/bin/amplicon_contingency_table.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amplicon_contingency_table.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### graph_plot.py

```bash
$ singularity exec <container> /usr/local/bin/graph_plot.py
$ podman run --it --rm --entrypoint /usr/local/bin/graph_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/graph_plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iqtree2

```bash
$ singularity exec <container> /usr/local/bin/iqtree2
$ podman run --it --rm --entrypoint /usr/local/bin/iqtree2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iqtree2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lambda

```bash
$ singularity exec <container> /usr/local/bin/lambda
$ podman run --it --rm --entrypoint /usr/local/bin/lambda   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lambda   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lambda_indexer

```bash
$ singularity exec <container> /usr/local/bin/lambda_indexer
$ podman run --it --rm --entrypoint /usr/local/bin/lambda_indexer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lambda_indexer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lotus2

```bash
$ singularity exec <container> /usr/local/bin/lotus2
$ podman run --it --rm --entrypoint /usr/local/bin/lotus2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lotus2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rdp_classifier

```bash
$ singularity exec <container> /usr/local/bin/rdp_classifier
$ podman run --it --rm --entrypoint /usr/local/bin/rdp_classifier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rdp_classifier   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rtk

```bash
$ singularity exec <container> /usr/local/bin/rtk
$ podman run --it --rm --entrypoint /usr/local/bin/rtk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rtk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdm

```bash
$ singularity exec <container> /usr/local/bin/sdm
$ podman run --it --rm --entrypoint /usr/local/bin/sdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### swarm

```bash
$ singularity exec <container> /usr/local/bin/swarm
$ podman run --it --rm --entrypoint /usr/local/bin/swarm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/swarm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clustalo

```bash
$ singularity exec <container> /usr/local/bin/clustalo
$ podman run --it --rm --entrypoint /usr/local/bin/clustalo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clustalo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zip

```bash
$ singularity exec <container> /usr/local/bin/zip
$ podman run --it --rm --entrypoint /usr/local/bin/zip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### iqtree

```bash
$ singularity exec <container> /usr/local/bin/iqtree
$ podman run --it --rm --entrypoint /usr/local/bin/iqtree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/iqtree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### funzip

```bash
$ singularity exec <container> /usr/local/bin/funzip
$ podman run --it --rm --entrypoint /usr/local/bin/funzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/funzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### igraph

```bash
$ singularity exec <container> /usr/local/bin/igraph
$ podman run --it --rm --entrypoint /usr/local/bin/igraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsearch

```bash
$ singularity exec <container> /usr/local/bin/vsearch
$ podman run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FET.pl

```bash
$ singularity exec <container> /usr/local/bin/FET.pl
$ podman run --it --rm --entrypoint /usr/local/bin/FET.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FET.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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