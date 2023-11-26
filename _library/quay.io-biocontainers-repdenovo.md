---
layout: container
name:  "quay.io/biocontainers/repdenovo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/repdenovo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/repdenovo/container.yaml"
updated_at: "2023-11-26 03:02:52.896827"
latest: "0.0.1--h0dced8c_3"
container_url: "https://biocontainers.pro/tools/repdenovo"
aliases:
 - "Assembly.py"
 - "BasicInfoPaser.py"
 - "ClassifyContigs.py"
 - "ContigsMerger"
 - "ExtractKmers.py"
 - "FilterAndScaffold.py"
 - "FilterPEReads.py"
 - "KmerCount.py"
 - "MergeContigs.py"
 - "TERefiner_1"
 - "Utility.py"
 - "main.py"
 - "velvetg"
 - "velveth"
 - "bamtools"
 - "jellyfish"
 - "qualfa2fq.pl"
 - "xa2multi.pl"
 - "bwa"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
versions:
 - "0.0.1--h4dc6686_2"
 - "0.0.1--h0dced8c_3"
description: "shpc-registry automated BioContainers addition for repdenovo"
config: {"url": "https://biocontainers.pro/tools/repdenovo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for repdenovo", "latest": {"0.0.1--h0dced8c_3": "sha256:5da6b571210594fe23bc19441cee715daa5b664c578116f263ca9e02c4cf1272"}, "tags": {"0.0.1--h4dc6686_2": "sha256:9fc82e46f70a77c0cec86668399750bbf0d30c2026013b6c95f8844c3e4b8336", "0.0.1--h0dced8c_3": "sha256:5da6b571210594fe23bc19441cee715daa5b664c578116f263ca9e02c4cf1272"}, "docker": "quay.io/biocontainers/repdenovo", "aliases": {"Assembly.py": "/usr/local/bin/Assembly.py", "BasicInfoPaser.py": "/usr/local/bin/BasicInfoPaser.py", "ClassifyContigs.py": "/usr/local/bin/ClassifyContigs.py", "ContigsMerger": "/usr/local/bin/ContigsMerger", "ExtractKmers.py": "/usr/local/bin/ExtractKmers.py", "FilterAndScaffold.py": "/usr/local/bin/FilterAndScaffold.py", "FilterPEReads.py": "/usr/local/bin/FilterPEReads.py", "KmerCount.py": "/usr/local/bin/KmerCount.py", "MergeContigs.py": "/usr/local/bin/MergeContigs.py", "TERefiner_1": "/usr/local/bin/TERefiner_1", "Utility.py": "/usr/local/bin/Utility.py", "main.py": "/usr/local/bin/main.py", "velvetg": "/usr/local/bin/velvetg", "velveth": "/usr/local/bin/velveth", "bamtools": "/usr/local/bin/bamtools", "jellyfish": "/usr/local/bin/jellyfish", "qualfa2fq.pl": "/usr/local/bin/qualfa2fq.pl", "xa2multi.pl": "/usr/local/bin/xa2multi.pl", "bwa": "/usr/local/bin/bwa", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/repdenovo.
shpc-registry automated BioContainers addition for repdenovo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/repdenovo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/repdenovo:0.0.1--h0dced8c_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/repdenovo/0.0.1--h0dced8c_3
$ module help quay.io/biocontainers/repdenovo/0.0.1--h0dced8c_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### repdenovo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### repdenovo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### repdenovo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### repdenovo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### repdenovo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### repdenovo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Assembly.py

```bash
$ singularity exec <container> /usr/local/bin/Assembly.py
$ podman run --it --rm --entrypoint /usr/local/bin/Assembly.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Assembly.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### BasicInfoPaser.py

```bash
$ singularity exec <container> /usr/local/bin/BasicInfoPaser.py
$ podman run --it --rm --entrypoint /usr/local/bin/BasicInfoPaser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/BasicInfoPaser.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ClassifyContigs.py

```bash
$ singularity exec <container> /usr/local/bin/ClassifyContigs.py
$ podman run --it --rm --entrypoint /usr/local/bin/ClassifyContigs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ClassifyContigs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ContigsMerger

```bash
$ singularity exec <container> /usr/local/bin/ContigsMerger
$ podman run --it --rm --entrypoint /usr/local/bin/ContigsMerger   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ContigsMerger   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ExtractKmers.py

```bash
$ singularity exec <container> /usr/local/bin/ExtractKmers.py
$ podman run --it --rm --entrypoint /usr/local/bin/ExtractKmers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ExtractKmers.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FilterAndScaffold.py

```bash
$ singularity exec <container> /usr/local/bin/FilterAndScaffold.py
$ podman run --it --rm --entrypoint /usr/local/bin/FilterAndScaffold.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FilterAndScaffold.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FilterPEReads.py

```bash
$ singularity exec <container> /usr/local/bin/FilterPEReads.py
$ podman run --it --rm --entrypoint /usr/local/bin/FilterPEReads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FilterPEReads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### KmerCount.py

```bash
$ singularity exec <container> /usr/local/bin/KmerCount.py
$ podman run --it --rm --entrypoint /usr/local/bin/KmerCount.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/KmerCount.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MergeContigs.py

```bash
$ singularity exec <container> /usr/local/bin/MergeContigs.py
$ podman run --it --rm --entrypoint /usr/local/bin/MergeContigs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MergeContigs.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TERefiner_1

```bash
$ singularity exec <container> /usr/local/bin/TERefiner_1
$ podman run --it --rm --entrypoint /usr/local/bin/TERefiner_1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TERefiner_1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Utility.py

```bash
$ singularity exec <container> /usr/local/bin/Utility.py
$ podman run --it --rm --entrypoint /usr/local/bin/Utility.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Utility.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### main.py

```bash
$ singularity exec <container> /usr/local/bin/main.py
$ podman run --it --rm --entrypoint /usr/local/bin/main.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/main.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### velvetg

```bash
$ singularity exec <container> /usr/local/bin/velvetg
$ podman run --it --rm --entrypoint /usr/local/bin/velvetg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/velvetg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### velveth

```bash
$ singularity exec <container> /usr/local/bin/velveth
$ podman run --it --rm --entrypoint /usr/local/bin/velveth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/velveth   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamtools

```bash
$ singularity exec <container> /usr/local/bin/bamtools
$ podman run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jellyfish

```bash
$ singularity exec <container> /usr/local/bin/jellyfish
$ podman run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qualfa2fq.pl

```bash
$ singularity exec <container> /usr/local/bin/qualfa2fq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/qualfa2fq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qualfa2fq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xa2multi.pl

```bash
$ singularity exec <container> /usr/local/bin/xa2multi.pl
$ podman run --it --rm --entrypoint /usr/local/bin/xa2multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xa2multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa

```bash
$ singularity exec <container> /usr/local/bin/bwa
$ podman run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
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