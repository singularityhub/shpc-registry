---
layout: container
name:  "quay.io/biocontainers/chronaeon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/chronaeon/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/chronaeon/container.yaml"
updated_at: "2026-10-10 19:16:22.886423"
latest: "0.1.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/chronaeon"
aliases:
 - "ShortestPathTN93"
 - "chronaeon"
 - "fasta_diff"
 - "fasta_digest"
 - "nucfreqsfasta"
 - "readreduce"
 - "selectreads"
 - "seqcoverage"
 - "seqdiff"
 - "tn93"
 - "tn93-cluster"
 - "hf"
 - "tiny-agents"
 - "huggingface-cli"
 - "protoc-35.1.0"
 - "protoc-gen-upb-35.1.0"
 - "protoc-gen-upb_minitable-35.1.0"
 - "protoc-gen-upbdefs-35.1.0"
 - "torchfrtrace"
 - "httpx"
 - "pybind11-config"
 - "idna"
 - "torch_shm_manager"
 - "protoc-gen-upb_minitable"
 - "fc-genconf"
 - "torchrun"
 - "isympy"
 - "protoc-gen-upb"
 - "protoc-gen-upbdefs"
 - "hwloc-gather-cpuid"
 - "hwloc-annotate"
 - "hwloc-bind"
 - "hwloc-calc"
 - "hwloc-compress-dir"
 - "hwloc-diff"
 - "hwloc-distrib"
versions:
 - "0.1.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for chronaeon"
config: {"url": "https://biocontainers.pro/tools/chronaeon", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for chronaeon", "latest": {"0.1.1--pyhdfd78af_0": "sha256:1a6e424fb496642485c0b7529004a756116a741130717a102beb8d9a36dea269"}, "tags": {"0.1.1--pyhdfd78af_0": "sha256:1a6e424fb496642485c0b7529004a756116a741130717a102beb8d9a36dea269"}, "docker": "quay.io/biocontainers/chronaeon", "aliases": {"ShortestPathTN93": "/usr/local/bin/ShortestPathTN93", "chronaeon": "/usr/local/bin/chronaeon", "fasta_diff": "/usr/local/bin/fasta_diff", "fasta_digest": "/usr/local/bin/fasta_digest", "nucfreqsfasta": "/usr/local/bin/nucfreqsfasta", "readreduce": "/usr/local/bin/readreduce", "selectreads": "/usr/local/bin/selectreads", "seqcoverage": "/usr/local/bin/seqcoverage", "seqdiff": "/usr/local/bin/seqdiff", "tn93": "/usr/local/bin/tn93", "tn93-cluster": "/usr/local/bin/tn93-cluster", "hf": "/usr/local/bin/hf", "tiny-agents": "/usr/local/bin/tiny-agents", "huggingface-cli": "/usr/local/bin/huggingface-cli", "protoc-35.1.0": "/usr/local/bin/protoc-35.1.0", "protoc-gen-upb-35.1.0": "/usr/local/bin/protoc-gen-upb-35.1.0", "protoc-gen-upb_minitable-35.1.0": "/usr/local/bin/protoc-gen-upb_minitable-35.1.0", "protoc-gen-upbdefs-35.1.0": "/usr/local/bin/protoc-gen-upbdefs-35.1.0", "torchfrtrace": "/usr/local/bin/torchfrtrace", "httpx": "/usr/local/bin/httpx", "pybind11-config": "/usr/local/bin/pybind11-config", "idna": "/usr/local/bin/idna", "torch_shm_manager": "/usr/local/bin/torch_shm_manager", "protoc-gen-upb_minitable": "/usr/local/bin/protoc-gen-upb_minitable", "fc-genconf": "/usr/local/bin/fc-genconf", "torchrun": "/usr/local/bin/torchrun", "isympy": "/usr/local/bin/isympy", "protoc-gen-upb": "/usr/local/bin/protoc-gen-upb", "protoc-gen-upbdefs": "/usr/local/bin/protoc-gen-upbdefs", "hwloc-gather-cpuid": "/usr/local/bin/hwloc-gather-cpuid", "hwloc-annotate": "/usr/local/bin/hwloc-annotate", "hwloc-bind": "/usr/local/bin/hwloc-bind", "hwloc-calc": "/usr/local/bin/hwloc-calc", "hwloc-compress-dir": "/usr/local/bin/hwloc-compress-dir", "hwloc-diff": "/usr/local/bin/hwloc-diff", "hwloc-distrib": "/usr/local/bin/hwloc-distrib"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/chronaeon.
singularity registry hpc automated addition for chronaeon
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/chronaeon
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/chronaeon:0.1.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/chronaeon/0.1.1--pyhdfd78af_0
$ module help quay.io/biocontainers/chronaeon/0.1.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### chronaeon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### chronaeon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### chronaeon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### chronaeon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### chronaeon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### chronaeon-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ShortestPathTN93

```bash
$ singularity exec <container> /usr/local/bin/ShortestPathTN93
$ podman run --it --rm --entrypoint /usr/local/bin/ShortestPathTN93   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ShortestPathTN93   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chronaeon

```bash
$ singularity exec <container> /usr/local/bin/chronaeon
$ podman run --it --rm --entrypoint /usr/local/bin/chronaeon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chronaeon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_diff

```bash
$ singularity exec <container> /usr/local/bin/fasta_diff
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta_digest

```bash
$ singularity exec <container> /usr/local/bin/fasta_digest
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_digest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_digest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nucfreqsfasta

```bash
$ singularity exec <container> /usr/local/bin/nucfreqsfasta
$ podman run --it --rm --entrypoint /usr/local/bin/nucfreqsfasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nucfreqsfasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readreduce

```bash
$ singularity exec <container> /usr/local/bin/readreduce
$ podman run --it --rm --entrypoint /usr/local/bin/readreduce   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readreduce   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### selectreads

```bash
$ singularity exec <container> /usr/local/bin/selectreads
$ podman run --it --rm --entrypoint /usr/local/bin/selectreads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/selectreads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqcoverage

```bash
$ singularity exec <container> /usr/local/bin/seqcoverage
$ podman run --it --rm --entrypoint /usr/local/bin/seqcoverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqcoverage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqdiff

```bash
$ singularity exec <container> /usr/local/bin/seqdiff
$ podman run --it --rm --entrypoint /usr/local/bin/seqdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tn93

```bash
$ singularity exec <container> /usr/local/bin/tn93
$ podman run --it --rm --entrypoint /usr/local/bin/tn93   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tn93   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tn93-cluster

```bash
$ singularity exec <container> /usr/local/bin/tn93-cluster
$ podman run --it --rm --entrypoint /usr/local/bin/tn93-cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tn93-cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hf

```bash
$ singularity exec <container> /usr/local/bin/hf
$ podman run --it --rm --entrypoint /usr/local/bin/hf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiny-agents

```bash
$ singularity exec <container> /usr/local/bin/tiny-agents
$ podman run --it --rm --entrypoint /usr/local/bin/tiny-agents   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tiny-agents   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### huggingface-cli

```bash
$ singularity exec <container> /usr/local/bin/huggingface-cli
$ podman run --it --rm --entrypoint /usr/local/bin/huggingface-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/huggingface-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-35.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-35.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb-35.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb-35.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb_minitable-35.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb_minitable-35.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upbdefs-35.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upbdefs-35.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-35.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchfrtrace

```bash
$ singularity exec <container> /usr/local/bin/torchfrtrace
$ podman run --it --rm --entrypoint /usr/local/bin/torchfrtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchfrtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### httpx

```bash
$ singularity exec <container> /usr/local/bin/httpx
$ podman run --it --rm --entrypoint /usr/local/bin/httpx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/httpx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybind11-config

```bash
$ singularity exec <container> /usr/local/bin/pybind11-config
$ podman run --it --rm --entrypoint /usr/local/bin/pybind11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybind11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idna

```bash
$ singularity exec <container> /usr/local/bin/idna
$ podman run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torch_shm_manager

```bash
$ singularity exec <container> /usr/local/bin/torch_shm_manager
$ podman run --it --rm --entrypoint /usr/local/bin/torch_shm_manager   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torch_shm_manager   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb_minitable

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb_minitable
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-genconf

```bash
$ singularity exec <container> /usr/local/bin/fc-genconf
$ podman run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchrun

```bash
$ singularity exec <container> /usr/local/bin/torchrun
$ podman run --it --rm --entrypoint /usr/local/bin/torchrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isympy

```bash
$ singularity exec <container> /usr/local/bin/isympy
$ podman run --it --rm --entrypoint /usr/local/bin/isympy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isympy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upbdefs

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upbdefs
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-gather-cpuid

```bash
$ singularity exec <container> /usr/local/bin/hwloc-gather-cpuid
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-gather-cpuid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-gather-cpuid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-annotate

```bash
$ singularity exec <container> /usr/local/bin/hwloc-annotate
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-bind

```bash
$ singularity exec <container> /usr/local/bin/hwloc-bind
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-bind   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-bind   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-calc

```bash
$ singularity exec <container> /usr/local/bin/hwloc-calc
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-calc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-calc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-compress-dir

```bash
$ singularity exec <container> /usr/local/bin/hwloc-compress-dir
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-compress-dir   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-compress-dir   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-diff

```bash
$ singularity exec <container> /usr/local/bin/hwloc-diff
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-distrib

```bash
$ singularity exec <container> /usr/local/bin/hwloc-distrib
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-distrib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-distrib   -v ${PWD} -w ${PWD} <container> -c " $@"
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