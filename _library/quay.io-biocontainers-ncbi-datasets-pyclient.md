---
layout: container
name:  "quay.io/biocontainers/ncbi-datasets-pyclient"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ncbi-datasets-pyclient/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ncbi-datasets-pyclient/container.yaml"
updated_at: "2026-03-26 05:32:44.810044"
latest: "18.20.0--pyh106432d_0"
container_url: "https://biocontainers.pro/tools/ncbi-datasets-pyclient"
aliases:
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
versions:
 - "17.3.0--pyh7e72e81_0"
 - "18.1.0--pyh7e72e81_0"
 - "18.0.5--pyh7e72e81_0"
 - "18.3.1--pyh7e72e81_0"
 - "18.2.3--pyh7e72e81_0"
 - "18.4.0--pyh7e72e81_0"
 - "18.13.0--pyh7e72e81_0"
 - "18.14.0--pyh7e72e81_0"
 - "18.17.1--pyh106432d_0"
 - "18.16.0--pyh7e72e81_0"
 - "18.15.0--pyh7e72e81_0"
 - "18.20.0--pyh106432d_0"
 - "18.19.0--pyh106432d_0"
 - "18.18.0--pyh106432d_0"
description: "singularity registry hpc automated addition for ncbi-datasets-pyclient"
config: {"url": "https://biocontainers.pro/tools/ncbi-datasets-pyclient", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ncbi-datasets-pyclient", "latest": {"18.20.0--pyh106432d_0": "sha256:69866526f25c160d1fad14a94cfec0d56c00299bdc4cf822f854d7c3719d66f6"}, "tags": {"17.3.0--pyh7e72e81_0": "sha256:a36f3f33dbea1df476c494b242b99e1fe677134d31cb47a8c7e75c9ba89e0037", "18.1.0--pyh7e72e81_0": "sha256:0910e01be4c90990aa0ce7d6fa6de477f38fbeb5e1cbafe6989689255eb03276", "18.0.5--pyh7e72e81_0": "sha256:dbc40d119e5c1ac91b5d205e6792d5246b4454874873e1f3409a239fc659426d", "18.3.1--pyh7e72e81_0": "sha256:5f41dc8102378820f2adf25b3756d948b5ebbaaff01a7ba305ca816f4457d138", "18.2.3--pyh7e72e81_0": "sha256:ed5cf42969b5f7d04fe54b478fa7fc29067ab79ef6eb037f5514f2db76047f11", "18.4.0--pyh7e72e81_0": "sha256:a8a77dc44f3ce3e61243da24d6f603d405e5acf708580c259977add817093d3b", "18.13.0--pyh7e72e81_0": "sha256:0c6c7932df43afe0c33443346fceb0ab7d162a14589c9576e128a83c3c095aad", "18.14.0--pyh7e72e81_0": "sha256:a79a77e369392c1249dd7058537df62fd3f97ac81aad4957f5fac81d4fb8a71f", "18.17.1--pyh106432d_0": "sha256:d34c2374ce3132a6b779fee83938f29534829c53abb88cca33697beeb4f2bf52", "18.16.0--pyh7e72e81_0": "sha256:ab00525cabd11d89760dddcbdea91385482032a76875ff976fabd9556859737c", "18.15.0--pyh7e72e81_0": "sha256:f561a6a0e1db61f8f8ffab86b450cfaa20a8ee7cb61be1cbc7ea0ee72ea90355", "18.20.0--pyh106432d_0": "sha256:69866526f25c160d1fad14a94cfec0d56c00299bdc4cf822f854d7c3719d66f6", "18.19.0--pyh106432d_0": "sha256:c6e3d785509f81a5a330e3602911756ea0207340dd0f20481be9bfa4b19e775d", "18.18.0--pyh106432d_0": "sha256:092fa9a812fca5336ffc23c6235572c4f19e09dd8b9bb19b9e13e56febf32aac"}, "docker": "quay.io/biocontainers/ncbi-datasets-pyclient", "aliases": {"idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ncbi-datasets-pyclient.
singularity registry hpc automated addition for ncbi-datasets-pyclient
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ncbi-datasets-pyclient
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ncbi-datasets-pyclient:18.20.0--pyh106432d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ncbi-datasets-pyclient/18.20.0--pyh106432d_0
$ module help quay.io/biocontainers/ncbi-datasets-pyclient/18.20.0--pyh106432d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ncbi-datasets-pyclient-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ncbi-datasets-pyclient-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ncbi-datasets-pyclient-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ncbi-datasets-pyclient-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ncbi-datasets-pyclient-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ncbi-datasets-pyclient-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### idle3.13

```bash
$ singularity exec <container> /usr/local/bin/idle3.13
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.13

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.13
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13

```bash
$ singularity exec <container> /usr/local/bin/python3.13
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13-config

```bash
$ singularity exec <container> /usr/local/bin/python3.13-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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