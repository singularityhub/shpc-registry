---
layout: container
name:  "quay.io/biocontainers/ska2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ska2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ska2/container.yaml"
updated_at: "2025-09-01 04:07:51.941761"
latest: "0.4.1--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/ska2"
aliases:
 - "ska"
versions:
 - "0.2.0--h4349ce8_0"
 - "0.2.3--h4349ce8_0"
 - "0.2.4--h4349ce8_0"
 - "0.3.0--h4349ce8_0"
 - "0.3.2--h4349ce8_0"
 - "0.3.4--h4349ce8_0"
 - "0.3.5--h4349ce8_0"
 - "0.3.6--h4349ce8_0"
 - "0.3.7--h4349ce8_0"
 - "0.3.7--h4349ce8_1"
 - "0.3.7--h4349ce8_2"
 - "0.3.8--h4349ce8_0"
 - "0.3.9--h4349ce8_0"
 - "0.3.10--h4349ce8_0"
 - "0.3.11--h4349ce8_0"
 - "0.4.0--h4349ce8_0"
 - "0.4.1--h4349ce8_0"
description: "singularity registry hpc automated addition for ska2"
config: {"url": "https://biocontainers.pro/tools/ska2", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ska2", "latest": {"0.4.1--h4349ce8_0": "sha256:31811c4b47dd949ab145ce3919785231fdd209e3de537ae3a6b36ecbc074d112"}, "tags": {"0.2.0--h4349ce8_0": "sha256:ac907e8f690bb947459c83e6a793a8b4baf053207e9f5de06d0dd43f3ae05ca1", "0.2.3--h4349ce8_0": "sha256:60f227a8f5c22ae96742b973e7efd221df68c1e0d9a88f103dcc1f4d6af57fe3", "0.2.4--h4349ce8_0": "sha256:993a23db4bc0face24c434a117d6d2600131eea07e949a56387b61ec20b327eb", "0.3.0--h4349ce8_0": "sha256:f11078e0975809140b132ff729e70c9fc06b53ed06b3b7c7893d5a0c9002a489", "0.3.2--h4349ce8_0": "sha256:491076aa549182ee018f9c5936b61a6c531ebd66ea557fb3ba9af27aacc5a6a7", "0.3.4--h4349ce8_0": "sha256:c50715b94c0a2be9cf8d5dbd7b8312c7266fb72f4798d002b7f9a60e622091bb", "0.3.5--h4349ce8_0": "sha256:5a82da003d35a4f6c3d855d312dc6f2d87b83849bcdb2f099d0304fc4ed8c152", "0.3.6--h4349ce8_0": "sha256:a171b0f961dd64f263bfe0895944c60fa4ce29a06df12fc6016449795085b08f", "0.3.7--h4349ce8_0": "sha256:9665e581c5964d73071b93e75afef93e744607642ba412ab56f769a7c8f732d6", "0.3.7--h4349ce8_1": "sha256:aaea11536b9fcec1f4ef7d62b43201670e4433b0f99d28b091cc3f2a383afde9", "0.3.7--h4349ce8_2": "sha256:0e0e67586b7e2e83835c8754b6875ca823a69f8fd87f093ff9396fff8a9e4cc6", "0.3.8--h4349ce8_0": "sha256:bb8e11f00ae0a9e3df024689b31d5ee2aa22d14442fa10900b545fcb85fb4d0f", "0.3.9--h4349ce8_0": "sha256:514ad5fe0fcee78dc24a367e91ca439575c7d3b4b5d35a3eddc4f5d3b27355e8", "0.3.10--h4349ce8_0": "sha256:cc082e7cbd685fd198144f1a57cb031f34382adf73b02447248abdb8cf7fc1b6", "0.3.11--h4349ce8_0": "sha256:b49cfa3b3ca0b5acc66a4325b95ac9e0c177ddc3ee7542365e10464d163b099f", "0.4.0--h4349ce8_0": "sha256:cd2a67f431825915bd82c283c0ee5f64de6d68bef91c68baed8a696a1957c7d6", "0.4.1--h4349ce8_0": "sha256:31811c4b47dd949ab145ce3919785231fdd209e3de537ae3a6b36ecbc074d112"}, "docker": "quay.io/biocontainers/ska2", "aliases": {"ska": "/usr/local/bin/ska"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ska2.
singularity registry hpc automated addition for ska2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ska2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ska2:0.4.1--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ska2/0.4.1--h4349ce8_0
$ module help quay.io/biocontainers/ska2/0.4.1--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ska2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ska2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ska2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ska2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ska2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ska2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ska

```bash
$ singularity exec <container> /usr/local/bin/ska
$ podman run --it --rm --entrypoint /usr/local/bin/ska   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ska   -v ${PWD} -w ${PWD} <container> -c " $@"
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