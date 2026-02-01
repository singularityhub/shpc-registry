---
layout: container
name:  "quay.io/biocontainers/antismash-lite"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/antismash-lite/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/antismash-lite/container.yaml"
updated_at: "2026-02-01 05:03:42.887486"
latest: "8.0.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/antismash-lite"
aliases:
 - "antismash"
 - "download-antismash-databases"
 - "hmmalign2"
 - "hmmbuild2"
 - "hmmc2"
 - "hmmcalibrate2"
 - "hmmconvert2"
 - "hmmemit2"
 - "hmmerfm-exactmatch"
 - "hmmfetch2"
 - "hmmindex2"
 - "hmmpfam2"
 - "hmmsearch2"
 - "less2scss"
 - "pyscss"
 - "xsltproc_lite"
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
versions:
 - "6.1.1--pyhdfd78af_0"
 - "6.1.1--pyhdfd78af_1"
 - "7.1.0--pyhdfd78af_0"
 - "8.0.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for antismash-lite"
config: {"url": "https://biocontainers.pro/tools/antismash-lite", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for antismash-lite", "latest": {"8.0.1--pyhdfd78af_0": "sha256:a58e82341c996b3423eedf90b6b54dd63f7712c50a7c83699c96120004d7e1bf"}, "tags": {"6.1.1--pyhdfd78af_0": "sha256:f5c47cde9daeb4788b33f554794da7fb5030b97658d960279d7ccf55112abb43", "6.1.1--pyhdfd78af_1": "sha256:52276bec2de30a3ba59ab9f18bd08d681299ac6bfc676c7cbb2b6a55c9ee33cc", "7.1.0--pyhdfd78af_0": "sha256:f5164b3127313d5f35829c9875f04ff3b26ebabd029b5205e4e86c9ba4c89af2", "8.0.1--pyhdfd78af_0": "sha256:a58e82341c996b3423eedf90b6b54dd63f7712c50a7c83699c96120004d7e1bf"}, "docker": "quay.io/biocontainers/antismash-lite", "aliases": {"antismash": "/usr/local/bin/antismash", "download-antismash-databases": "/usr/local/bin/download-antismash-databases", "hmmalign2": "/usr/local/bin/hmmalign2", "hmmbuild2": "/usr/local/bin/hmmbuild2", "hmmc2": "/usr/local/bin/hmmc2", "hmmcalibrate2": "/usr/local/bin/hmmcalibrate2", "hmmconvert2": "/usr/local/bin/hmmconvert2", "hmmemit2": "/usr/local/bin/hmmemit2", "hmmerfm-exactmatch": "/usr/local/bin/hmmerfm-exactmatch", "hmmfetch2": "/usr/local/bin/hmmfetch2", "hmmindex2": "/usr/local/bin/hmmindex2", "hmmpfam2": "/usr/local/bin/hmmpfam2", "hmmsearch2": "/usr/local/bin/hmmsearch2", "less2scss": "/usr/local/bin/less2scss", "pyscss": "/usr/local/bin/pyscss", "xsltproc_lite": "/usr/local/bin/xsltproc_lite", "alphtype": "/usr/local/bin/alphtype", "ama": "/usr/local/bin/ama", "ama-qvalues": "/usr/local/bin/ama-qvalues", "ame": "/usr/local/bin/ame", "beeml2meme": "/usr/local/bin/beeml2meme", "centrimo": "/usr/local/bin/centrimo", "ceqlogo": "/usr/local/bin/ceqlogo", "chen2meme": "/usr/local/bin/chen2meme", "clustalw2fasta": "/usr/local/bin/clustalw2fasta", "clustalw2phylip": "/usr/local/bin/clustalw2phylip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/antismash-lite.
shpc-registry automated BioContainers addition for antismash-lite
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/antismash-lite
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/antismash-lite:8.0.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/antismash-lite/8.0.1--pyhdfd78af_0
$ module help quay.io/biocontainers/antismash-lite/8.0.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### antismash-lite-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### antismash-lite-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### antismash-lite-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### antismash-lite-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### antismash-lite-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### antismash-lite-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### antismash

```bash
$ singularity exec <container> /usr/local/bin/antismash
$ podman run --it --rm --entrypoint /usr/local/bin/antismash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/antismash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download-antismash-databases

```bash
$ singularity exec <container> /usr/local/bin/download-antismash-databases
$ podman run --it --rm --entrypoint /usr/local/bin/download-antismash-databases   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download-antismash-databases   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmalign2

```bash
$ singularity exec <container> /usr/local/bin/hmmalign2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmalign2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmalign2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmbuild2

```bash
$ singularity exec <container> /usr/local/bin/hmmbuild2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmbuild2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmbuild2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmc2

```bash
$ singularity exec <container> /usr/local/bin/hmmc2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmc2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmc2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmcalibrate2

```bash
$ singularity exec <container> /usr/local/bin/hmmcalibrate2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmcalibrate2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmcalibrate2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmconvert2

```bash
$ singularity exec <container> /usr/local/bin/hmmconvert2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmconvert2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmconvert2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmemit2

```bash
$ singularity exec <container> /usr/local/bin/hmmemit2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmemit2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmemit2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmerfm-exactmatch

```bash
$ singularity exec <container> /usr/local/bin/hmmerfm-exactmatch
$ podman run --it --rm --entrypoint /usr/local/bin/hmmerfm-exactmatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmerfm-exactmatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmfetch2

```bash
$ singularity exec <container> /usr/local/bin/hmmfetch2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmfetch2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmfetch2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmindex2

```bash
$ singularity exec <container> /usr/local/bin/hmmindex2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmindex2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmindex2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmpfam2

```bash
$ singularity exec <container> /usr/local/bin/hmmpfam2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmpfam2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmpfam2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmsearch2

```bash
$ singularity exec <container> /usr/local/bin/hmmsearch2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmsearch2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmsearch2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### less2scss

```bash
$ singularity exec <container> /usr/local/bin/less2scss
$ podman run --it --rm --entrypoint /usr/local/bin/less2scss   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/less2scss   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyscss

```bash
$ singularity exec <container> /usr/local/bin/pyscss
$ podman run --it --rm --entrypoint /usr/local/bin/pyscss   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyscss   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xsltproc_lite

```bash
$ singularity exec <container> /usr/local/bin/xsltproc_lite
$ podman run --it --rm --entrypoint /usr/local/bin/xsltproc_lite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xsltproc_lite   -v ${PWD} -w ${PWD} <container> -c " $@"
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