---
layout: container
name:  "quay.io/biocontainers/vhamster"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vhamster/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vhamster/container.yaml"
updated_at: "2026-10-10 19:34:59.448885"
latest: "1.3.1--pyh106432d_0"
container_url: "https://biocontainers.pro/tools/vhamster"
aliases:
 - "accelerate"
 - "accelerate-config"
 - "accelerate-estimate-memory"
 - "accelerate-launch"
 - "accelerate-merge-weights"
 - "vhamster"
 - "vhamster-features"
 - "vhamster-install-models"
 - "pyrodigal-gv"
 - "transformers"
 - "hf"
 - "tiny-agents"
 - "huggingface-cli"
 - "protoc-35.1.0"
 - "protoc-gen-upb-35.1.0"
 - "protoc-gen-upb_minitable-35.1.0"
 - "protoc-gen-upbdefs-35.1.0"
 - "pyrodigal"
 - "archspec"
 - "torchfrtrace"
 - "httpx"
 - "pybind11-config"
 - "idna"
 - "torch_shm_manager"
 - "typer"
 - "protoc-gen-upb_minitable"
 - "torchrun"
 - "isympy"
 - "protoc-gen-upb"
 - "protoc-gen-upbdefs"
 - "markdown-it"
 - "hwloc-gather-cpuid"
 - "hwloc-annotate"
versions:
 - "1.3.1--pyh106432d_0"
description: "singularity registry hpc automated addition for vhamster"
config: {"url": "https://biocontainers.pro/tools/vhamster", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for vhamster", "latest": {"1.3.1--pyh106432d_0": "sha256:ae63a3bb8c7dac40c2107e42fbec15db6f85878e8211930c232a832089d04295"}, "tags": {"1.3.1--pyh106432d_0": "sha256:ae63a3bb8c7dac40c2107e42fbec15db6f85878e8211930c232a832089d04295"}, "docker": "quay.io/biocontainers/vhamster", "aliases": {"accelerate": "/usr/local/bin/accelerate", "accelerate-config": "/usr/local/bin/accelerate-config", "accelerate-estimate-memory": "/usr/local/bin/accelerate-estimate-memory", "accelerate-launch": "/usr/local/bin/accelerate-launch", "accelerate-merge-weights": "/usr/local/bin/accelerate-merge-weights", "vhamster": "/usr/local/bin/vhamster", "vhamster-features": "/usr/local/bin/vhamster-features", "vhamster-install-models": "/usr/local/bin/vhamster-install-models", "pyrodigal-gv": "/usr/local/bin/pyrodigal-gv", "transformers": "/usr/local/bin/transformers", "hf": "/usr/local/bin/hf", "tiny-agents": "/usr/local/bin/tiny-agents", "huggingface-cli": "/usr/local/bin/huggingface-cli", "protoc-35.1.0": "/usr/local/bin/protoc-35.1.0", "protoc-gen-upb-35.1.0": "/usr/local/bin/protoc-gen-upb-35.1.0", "protoc-gen-upb_minitable-35.1.0": "/usr/local/bin/protoc-gen-upb_minitable-35.1.0", "protoc-gen-upbdefs-35.1.0": "/usr/local/bin/protoc-gen-upbdefs-35.1.0", "pyrodigal": "/usr/local/bin/pyrodigal", "archspec": "/usr/local/bin/archspec", "torchfrtrace": "/usr/local/bin/torchfrtrace", "httpx": "/usr/local/bin/httpx", "pybind11-config": "/usr/local/bin/pybind11-config", "idna": "/usr/local/bin/idna", "torch_shm_manager": "/usr/local/bin/torch_shm_manager", "typer": "/usr/local/bin/typer", "protoc-gen-upb_minitable": "/usr/local/bin/protoc-gen-upb_minitable", "torchrun": "/usr/local/bin/torchrun", "isympy": "/usr/local/bin/isympy", "protoc-gen-upb": "/usr/local/bin/protoc-gen-upb", "protoc-gen-upbdefs": "/usr/local/bin/protoc-gen-upbdefs", "markdown-it": "/usr/local/bin/markdown-it", "hwloc-gather-cpuid": "/usr/local/bin/hwloc-gather-cpuid", "hwloc-annotate": "/usr/local/bin/hwloc-annotate"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vhamster.
singularity registry hpc automated addition for vhamster
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vhamster
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vhamster:1.3.1--pyh106432d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vhamster/1.3.1--pyh106432d_0
$ module help quay.io/biocontainers/vhamster/1.3.1--pyh106432d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vhamster-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vhamster-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vhamster-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vhamster-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vhamster-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vhamster-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### accelerate

```bash
$ singularity exec <container> /usr/local/bin/accelerate
$ podman run --it --rm --entrypoint /usr/local/bin/accelerate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/accelerate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### accelerate-config

```bash
$ singularity exec <container> /usr/local/bin/accelerate-config
$ podman run --it --rm --entrypoint /usr/local/bin/accelerate-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/accelerate-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### accelerate-estimate-memory

```bash
$ singularity exec <container> /usr/local/bin/accelerate-estimate-memory
$ podman run --it --rm --entrypoint /usr/local/bin/accelerate-estimate-memory   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/accelerate-estimate-memory   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### accelerate-launch

```bash
$ singularity exec <container> /usr/local/bin/accelerate-launch
$ podman run --it --rm --entrypoint /usr/local/bin/accelerate-launch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/accelerate-launch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### accelerate-merge-weights

```bash
$ singularity exec <container> /usr/local/bin/accelerate-merge-weights
$ podman run --it --rm --entrypoint /usr/local/bin/accelerate-merge-weights   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/accelerate-merge-weights   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vhamster

```bash
$ singularity exec <container> /usr/local/bin/vhamster
$ podman run --it --rm --entrypoint /usr/local/bin/vhamster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vhamster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vhamster-features

```bash
$ singularity exec <container> /usr/local/bin/vhamster-features
$ podman run --it --rm --entrypoint /usr/local/bin/vhamster-features   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vhamster-features   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vhamster-install-models

```bash
$ singularity exec <container> /usr/local/bin/vhamster-install-models
$ podman run --it --rm --entrypoint /usr/local/bin/vhamster-install-models   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vhamster-install-models   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrodigal-gv

```bash
$ singularity exec <container> /usr/local/bin/pyrodigal-gv
$ podman run --it --rm --entrypoint /usr/local/bin/pyrodigal-gv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrodigal-gv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transformers

```bash
$ singularity exec <container> /usr/local/bin/transformers
$ podman run --it --rm --entrypoint /usr/local/bin/transformers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transformers   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pyrodigal

```bash
$ singularity exec <container> /usr/local/bin/pyrodigal
$ podman run --it --rm --entrypoint /usr/local/bin/pyrodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archspec

```bash
$ singularity exec <container> /usr/local/bin/archspec
$ podman run --it --rm --entrypoint /usr/local/bin/archspec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archspec   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### typer

```bash
$ singularity exec <container> /usr/local/bin/typer
$ podman run --it --rm --entrypoint /usr/local/bin/typer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/typer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb_minitable

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb_minitable
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### markdown-it

```bash
$ singularity exec <container> /usr/local/bin/markdown-it
$ podman run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
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