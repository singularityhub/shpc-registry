---
layout: container
name:  "quay.io/biocontainers/pyamilyseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyamilyseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pyamilyseq/container.yaml"
updated_at: "2025-11-21 03:19:33.921607"
latest: "1.3.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/pyamilyseq"
aliases:
 - "Group-Extractor"
 - "Group-Splitter"
 - "Group-Summary"
 - "PyamilySeq"
 - "Seq-Combiner"
 - "Seq-Extractor"
 - "Seq-Finder"
 - "compare-contree-singletrees"
 - "compare-rf"
 - "compute-singletrees-rf"
 - "group-extractor"
 - "group-splitter"
 - "group-summary"
 - "pyamilyseq"
 - "seq-combiner"
 - "seq-extractor"
 - "seq-finder"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
 - "numpy-config"
versions:
 - "1.3.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for pyamilyseq"
config: {"url": "https://biocontainers.pro/tools/pyamilyseq", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pyamilyseq", "latest": {"1.3.2--pyhdfd78af_0": "sha256:204722a2128f73b80075b22a37a57ec21869f9c6f4255a2eb57004d156731595"}, "tags": {"1.3.2--pyhdfd78af_0": "sha256:204722a2128f73b80075b22a37a57ec21869f9c6f4255a2eb57004d156731595"}, "docker": "quay.io/biocontainers/pyamilyseq", "aliases": {"Group-Extractor": "/usr/local/bin/Group-Extractor", "Group-Splitter": "/usr/local/bin/Group-Splitter", "Group-Summary": "/usr/local/bin/Group-Summary", "PyamilySeq": "/usr/local/bin/PyamilySeq", "Seq-Combiner": "/usr/local/bin/Seq-Combiner", "Seq-Extractor": "/usr/local/bin/Seq-Extractor", "Seq-Finder": "/usr/local/bin/Seq-Finder", "compare-contree-singletrees": "/usr/local/bin/compare-contree-singletrees", "compare-rf": "/usr/local/bin/compare-rf", "compute-singletrees-rf": "/usr/local/bin/compute-singletrees-rf", "group-extractor": "/usr/local/bin/group-extractor", "group-splitter": "/usr/local/bin/group-splitter", "group-summary": "/usr/local/bin/group-summary", "pyamilyseq": "/usr/local/bin/pyamilyseq", "seq-combiner": "/usr/local/bin/seq-combiner", "seq-extractor": "/usr/local/bin/seq-extractor", "seq-finder": "/usr/local/bin/seq-finder", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config", "numpy-config": "/usr/local/bin/numpy-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyamilyseq.
singularity registry hpc automated addition for pyamilyseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyamilyseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyamilyseq:1.3.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyamilyseq/1.3.2--pyhdfd78af_0
$ module help quay.io/biocontainers/pyamilyseq/1.3.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyamilyseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyamilyseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyamilyseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyamilyseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyamilyseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyamilyseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Group-Extractor

```bash
$ singularity exec <container> /usr/local/bin/Group-Extractor
$ podman run --it --rm --entrypoint /usr/local/bin/Group-Extractor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Group-Extractor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Group-Splitter

```bash
$ singularity exec <container> /usr/local/bin/Group-Splitter
$ podman run --it --rm --entrypoint /usr/local/bin/Group-Splitter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Group-Splitter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Group-Summary

```bash
$ singularity exec <container> /usr/local/bin/Group-Summary
$ podman run --it --rm --entrypoint /usr/local/bin/Group-Summary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Group-Summary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PyamilySeq

```bash
$ singularity exec <container> /usr/local/bin/PyamilySeq
$ podman run --it --rm --entrypoint /usr/local/bin/PyamilySeq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PyamilySeq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Seq-Combiner

```bash
$ singularity exec <container> /usr/local/bin/Seq-Combiner
$ podman run --it --rm --entrypoint /usr/local/bin/Seq-Combiner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Seq-Combiner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Seq-Extractor

```bash
$ singularity exec <container> /usr/local/bin/Seq-Extractor
$ podman run --it --rm --entrypoint /usr/local/bin/Seq-Extractor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Seq-Extractor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Seq-Finder

```bash
$ singularity exec <container> /usr/local/bin/Seq-Finder
$ podman run --it --rm --entrypoint /usr/local/bin/Seq-Finder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Seq-Finder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compare-contree-singletrees

```bash
$ singularity exec <container> /usr/local/bin/compare-contree-singletrees
$ podman run --it --rm --entrypoint /usr/local/bin/compare-contree-singletrees   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compare-contree-singletrees   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compare-rf

```bash
$ singularity exec <container> /usr/local/bin/compare-rf
$ podman run --it --rm --entrypoint /usr/local/bin/compare-rf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compare-rf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compute-singletrees-rf

```bash
$ singularity exec <container> /usr/local/bin/compute-singletrees-rf
$ podman run --it --rm --entrypoint /usr/local/bin/compute-singletrees-rf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compute-singletrees-rf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### group-extractor

```bash
$ singularity exec <container> /usr/local/bin/group-extractor
$ podman run --it --rm --entrypoint /usr/local/bin/group-extractor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/group-extractor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### group-splitter

```bash
$ singularity exec <container> /usr/local/bin/group-splitter
$ podman run --it --rm --entrypoint /usr/local/bin/group-splitter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/group-splitter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### group-summary

```bash
$ singularity exec <container> /usr/local/bin/group-summary
$ podman run --it --rm --entrypoint /usr/local/bin/group-summary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/group-summary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyamilyseq

```bash
$ singularity exec <container> /usr/local/bin/pyamilyseq
$ podman run --it --rm --entrypoint /usr/local/bin/pyamilyseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyamilyseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seq-combiner

```bash
$ singularity exec <container> /usr/local/bin/seq-combiner
$ podman run --it --rm --entrypoint /usr/local/bin/seq-combiner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seq-combiner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seq-extractor

```bash
$ singularity exec <container> /usr/local/bin/seq-extractor
$ podman run --it --rm --entrypoint /usr/local/bin/seq-extractor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seq-extractor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seq-finder

```bash
$ singularity exec <container> /usr/local/bin/seq-finder
$ podman run --it --rm --entrypoint /usr/local/bin/seq-finder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seq-finder   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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