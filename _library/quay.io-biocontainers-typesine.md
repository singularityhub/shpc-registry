---
layout: container
name:  "quay.io/biocontainers/typesine"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/typesine/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/typesine/container.yaml"
updated_at: "2026-08-16 04:02:25.744975"
latest: "1.0.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/typesine"
aliases:
 - "seq_cache_populate.py"
 - "typesine"
 - "bwa-mem2"
 - "bwa-mem2.avx"
 - "bwa-mem2.avx2"
 - "bwa-mem2.avx512bw"
 - "bwa-mem2.sse41"
 - "bwa-mem2.sse42"
 - "ref-cache"
 - "annot-tsv"
 - "shiftBed"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
 - "annotateBed"
 - "bamToBed"
 - "bamToFastq"
 - "bed12ToBed6"
 - "bedToBam"
 - "bedToIgv"
 - "bedpeToBam"
 - "bedtools"
 - "closestBed"
 - "clusterBed"
 - "complementBed"
 - "coverageBed"
versions:
 - "1.0.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for typesine"
config: {"url": "https://biocontainers.pro/tools/typesine", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for typesine", "latest": {"1.0.0--pyhdfd78af_0": "sha256:1fe42c093115f87173389466db67d404904b7afd7362704f25df088933ea926c"}, "tags": {"1.0.0--pyhdfd78af_0": "sha256:1fe42c093115f87173389466db67d404904b7afd7362704f25df088933ea926c"}, "docker": "quay.io/biocontainers/typesine", "aliases": {"seq_cache_populate.py": "/usr/local/bin/seq_cache_populate.py", "typesine": "/usr/local/bin/typesine", "bwa-mem2": "/usr/local/bin/bwa-mem2", "bwa-mem2.avx": "/usr/local/bin/bwa-mem2.avx", "bwa-mem2.avx2": "/usr/local/bin/bwa-mem2.avx2", "bwa-mem2.avx512bw": "/usr/local/bin/bwa-mem2.avx512bw", "bwa-mem2.sse41": "/usr/local/bin/bwa-mem2.sse41", "bwa-mem2.sse42": "/usr/local/bin/bwa-mem2.sse42", "ref-cache": "/usr/local/bin/ref-cache", "annot-tsv": "/usr/local/bin/annot-tsv", "shiftBed": "/usr/local/bin/shiftBed", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config", "annotateBed": "/usr/local/bin/annotateBed", "bamToBed": "/usr/local/bin/bamToBed", "bamToFastq": "/usr/local/bin/bamToFastq", "bed12ToBed6": "/usr/local/bin/bed12ToBed6", "bedToBam": "/usr/local/bin/bedToBam", "bedToIgv": "/usr/local/bin/bedToIgv", "bedpeToBam": "/usr/local/bin/bedpeToBam", "bedtools": "/usr/local/bin/bedtools", "closestBed": "/usr/local/bin/closestBed", "clusterBed": "/usr/local/bin/clusterBed", "complementBed": "/usr/local/bin/complementBed", "coverageBed": "/usr/local/bin/coverageBed"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/typesine.
singularity registry hpc automated addition for typesine
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/typesine
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/typesine:1.0.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/typesine/1.0.0--pyhdfd78af_0
$ module help quay.io/biocontainers/typesine/1.0.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### typesine-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### typesine-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### typesine-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### typesine-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### typesine-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### typesine-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### seq_cache_populate.py

```bash
$ singularity exec <container> /usr/local/bin/seq_cache_populate.py
$ podman run --it --rm --entrypoint /usr/local/bin/seq_cache_populate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seq_cache_populate.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### typesine

```bash
$ singularity exec <container> /usr/local/bin/typesine
$ podman run --it --rm --entrypoint /usr/local/bin/typesine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/typesine   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-mem2

```bash
$ singularity exec <container> /usr/local/bin/bwa-mem2
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-mem2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-mem2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-mem2.avx

```bash
$ singularity exec <container> /usr/local/bin/bwa-mem2.avx
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-mem2.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-mem2.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-mem2.avx2

```bash
$ singularity exec <container> /usr/local/bin/bwa-mem2.avx2
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-mem2.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-mem2.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-mem2.avx512bw

```bash
$ singularity exec <container> /usr/local/bin/bwa-mem2.avx512bw
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-mem2.avx512bw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-mem2.avx512bw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-mem2.sse41

```bash
$ singularity exec <container> /usr/local/bin/bwa-mem2.sse41
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-mem2.sse41   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-mem2.sse41   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-mem2.sse42

```bash
$ singularity exec <container> /usr/local/bin/bwa-mem2.sse42
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-mem2.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-mem2.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ref-cache

```bash
$ singularity exec <container> /usr/local/bin/ref-cache
$ podman run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiftBed

```bash
$ singularity exec <container> /usr/local/bin/shiftBed
$ podman run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.14

```bash
$ singularity exec <container> /usr/local/bin/idle3.14
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.14

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.14
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14

```bash
$ singularity exec <container> /usr/local/bin/python3.14
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14-config

```bash
$ singularity exec <container> /usr/local/bin/python3.14-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotateBed

```bash
$ singularity exec <container> /usr/local/bin/annotateBed
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToBed

```bash
$ singularity exec <container> /usr/local/bin/bamToBed
$ podman run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToFastq

```bash
$ singularity exec <container> /usr/local/bin/bamToFastq
$ podman run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed12ToBed6

```bash
$ singularity exec <container> /usr/local/bin/bed12ToBed6
$ podman run --it --rm --entrypoint /usr/local/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToBam

```bash
$ singularity exec <container> /usr/local/bin/bedToBam
$ podman run --it --rm --entrypoint /usr/local/bin/bedToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToIgv

```bash
$ singularity exec <container> /usr/local/bin/bedToIgv
$ podman run --it --rm --entrypoint /usr/local/bin/bedToIgv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToIgv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedpeToBam

```bash
$ singularity exec <container> /usr/local/bin/bedpeToBam
$ podman run --it --rm --entrypoint /usr/local/bin/bedpeToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedpeToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedtools

```bash
$ singularity exec <container> /usr/local/bin/bedtools
$ podman run --it --rm --entrypoint /usr/local/bin/bedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### closestBed

```bash
$ singularity exec <container> /usr/local/bin/closestBed
$ podman run --it --rm --entrypoint /usr/local/bin/closestBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/closestBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clusterBed

```bash
$ singularity exec <container> /usr/local/bin/clusterBed
$ podman run --it --rm --entrypoint /usr/local/bin/clusterBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clusterBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### complementBed

```bash
$ singularity exec <container> /usr/local/bin/complementBed
$ podman run --it --rm --entrypoint /usr/local/bin/complementBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/complementBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverageBed

```bash
$ singularity exec <container> /usr/local/bin/coverageBed
$ podman run --it --rm --entrypoint /usr/local/bin/coverageBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverageBed   -v ${PWD} -w ${PWD} <container> -c " $@"
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