---
layout: container
name:  "quay.io/biocontainers/miniprot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/miniprot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/miniprot/container.yaml"
updated_at: "2025-03-29 03:39:35.547808"
latest: "0.14--h577a1d6_0"
container_url: "https://biocontainers.pro/tools/miniprot"
aliases:
 - "miniprot"
versions:
 - "0.4--h7132678_0"
 - "0.5--h7132678_0"
 - "0.7--h7132678_0"
 - "0.6--h7132678_0"
 - "0.11--h7132678_0"
 - "0.10--h7132678_0"
 - "0.9--h7132678_0"
 - "0.8--h7132678_0"
 - "0.11--he4a0461_2"
 - "0.12--he4a0461_0"
 - "0.13--he4a0461_0"
 - "0.13--he4a0461_1"
 - "0.13--h577a1d6_2"
 - "0.14--h577a1d6_0"
description: "shpc-registry automated BioContainers addition for miniprot"
config: {"url": "https://biocontainers.pro/tools/miniprot", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for miniprot", "latest": {"0.14--h577a1d6_0": "sha256:0e7f58fa9e28057352ba29b85cc8765eca6ce76f0fe9a20bd899e94559689570"}, "tags": {"0.4--h7132678_0": "sha256:f47e9f65bc7e6abcd7e1d73dc505a737bcac805514ab44f2d7aa1a97c7d95ebd", "0.5--h7132678_0": "sha256:f2470b9f18f7c6765547e4e1429f04166238454aa0625204ea73d217743e48d9", "0.7--h7132678_0": "sha256:f6b9122f4bc36cabea25c5c81f17711d37b60b235a6c3e8e04e5979e51079c5e", "0.6--h7132678_0": "sha256:81a3a45c40ccc3d8875d0f512654dc20b91aa9a6f2e8ec1962efdbc24a80226e", "0.11--h7132678_0": "sha256:17ea7efdb2f167f6817308fe590f14454b11b23394c971d419c7d3c5a85882da", "0.10--h7132678_0": "sha256:87dba9d874fe10419c821f93afcaf4e1e734b06d917c5363f800bbb248430915", "0.9--h7132678_0": "sha256:e06fc9044e12dfc5ead39e4876996cf2f1f62a5addccd8232838ea0a028b866e", "0.8--h7132678_0": "sha256:57e5837b0f7dd72ee1019020b6ebe5179c3a88a5245cd9b580015a2bf38225e8", "0.11--he4a0461_2": "sha256:1958c9a031388ae33fc2f25adc29ea80ae917e13fc86b1d2d235481309f4d87a", "0.12--he4a0461_0": "sha256:c09c7fad96051c08f0525e2e80bacc14084da021f5e153fd604d463f255fda77", "0.13--he4a0461_0": "sha256:41e9fac359d2dfde9db33ad975ec08ca241c56371624608694887756e6a5205a", "0.13--he4a0461_1": "sha256:2e2b8f93d139949fd15bf6587b94274c7a86e33157312db9cb539c9e29100416", "0.13--h577a1d6_2": "sha256:0f472140aa291454d146998cb706649a27c55c14e4c78c89803e1175e46748bb", "0.14--h577a1d6_0": "sha256:0e7f58fa9e28057352ba29b85cc8765eca6ce76f0fe9a20bd899e94559689570"}, "docker": "quay.io/biocontainers/miniprot", "aliases": {"miniprot": "/usr/local/bin/miniprot"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/miniprot.
shpc-registry automated BioContainers addition for miniprot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/miniprot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/miniprot:0.14--h577a1d6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/miniprot/0.14--h577a1d6_0
$ module help quay.io/biocontainers/miniprot/0.14--h577a1d6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### miniprot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### miniprot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### miniprot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### miniprot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### miniprot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### miniprot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### miniprot

```bash
$ singularity exec <container> /usr/local/bin/miniprot
$ podman run --it --rm --entrypoint /usr/local/bin/miniprot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miniprot   -v ${PWD} -w ${PWD} <container> -c " $@"
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