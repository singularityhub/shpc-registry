---
layout: container
name:  "quay.io/biocontainers/grz-cli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/grz-cli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/grz-cli/container.yaml"
updated_at: "2025-09-19 03:08:21.574887"
latest: "1.2.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/grz-cli"
aliases:
 - "crypt4gh"
 - "crypt4gh-keygen"
 - "grz-cli"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "jp.py"
 - "jsonschema"
 - "tqdm"
versions:
 - "0.1.1--pyhdfd78af_0"
 - "0.1.4--pyhdfd78af_0"
 - "0.3.0--pyhdfd78af_0"
 - "0.5.0--pyhdfd78af_0"
 - "0.4.0--pyhdfd78af_0"
 - "0.6.0--pyhdfd78af_0"
 - "1.0.1--pyhdfd78af_0"
 - "0.7.0--pyhdfd78af_0"
 - "0.6.1--pyhdfd78af_0"
 - "1.1.1--pyhdfd78af_0"
 - "1.0.3--pyhdfd78af_0"
 - "1.2.0--pyhdfd78af_0"
 - "1.1.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for grz-cli"
config: {"url": "https://biocontainers.pro/tools/grz-cli", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for grz-cli", "latest": {"1.2.0--pyhdfd78af_0": "sha256:1efb97dcaa44684f20960f2a5fbdf3022733c6d3539c00b62ac6e483ac8a4b76"}, "tags": {"0.1.1--pyhdfd78af_0": "sha256:3d1d63ab7ff383a0cb440daa3f861042eb043745416cf1caeef8ee06cede240c", "0.1.4--pyhdfd78af_0": "sha256:637966566acc168f4ed8b15c639a7c108fd87e254220da177591ba6430cf0cf7", "0.3.0--pyhdfd78af_0": "sha256:e5580d39786198f8605153a7f7c393897de6ffb1a02f8759b0afc5d97de857cf", "0.5.0--pyhdfd78af_0": "sha256:9d05b6e024b93d0b3265f7bd16701bb593ac1eb1478e0d2ff7c8d4f26046d4a4", "0.4.0--pyhdfd78af_0": "sha256:4b3bc40c957ec8aafc196d984385e820acaf028f9c85a8692af55bcbc6ba1232", "0.6.0--pyhdfd78af_0": "sha256:cda922e9ba159e7661f06066c1c07fc61f77ef38d39299a837bc02f4291d709d", "1.0.1--pyhdfd78af_0": "sha256:cd535b9838acdbfa02fc3bd7b208fae5da5214c9e316353238301077848ba96d", "0.7.0--pyhdfd78af_0": "sha256:9d603b78c034599573b3d2c37d64b2b94b516e2abcbfb31dbf6c14929d1e17c2", "0.6.1--pyhdfd78af_0": "sha256:5afd937bff63e4281dbb72669f18f32c86da3fd9c034c1443ff036bede0bf5f1", "1.1.1--pyhdfd78af_0": "sha256:d99f656038cbc3f630c7dbaf3d2721ff39ccd2ba2f8d38e1d0c473b8d06b10c7", "1.0.3--pyhdfd78af_0": "sha256:9ced6e68ca189a569e03391ed3dd0c9cdc5b6b28b31b908661f363ad6e368d01", "1.2.0--pyhdfd78af_0": "sha256:1efb97dcaa44684f20960f2a5fbdf3022733c6d3539c00b62ac6e483ac8a4b76", "1.1.2--pyhdfd78af_0": "sha256:242ae4cfc34c6939faf2cb9789b9e852832d3e36b9d118063afb61935a9f4bdd"}, "docker": "quay.io/biocontainers/grz-cli", "aliases": {"crypt4gh": "/usr/local/bin/crypt4gh", "crypt4gh-keygen": "/usr/local/bin/crypt4gh-keygen", "grz-cli": "/usr/local/bin/grz-cli", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "jp.py": "/usr/local/bin/jp.py", "jsonschema": "/usr/local/bin/jsonschema", "tqdm": "/usr/local/bin/tqdm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/grz-cli.
singularity registry hpc automated addition for grz-cli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/grz-cli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/grz-cli:1.2.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/grz-cli/1.2.0--pyhdfd78af_0
$ module help quay.io/biocontainers/grz-cli/1.2.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### grz-cli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### grz-cli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### grz-cli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### grz-cli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### grz-cli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### grz-cli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### crypt4gh

```bash
$ singularity exec <container> /usr/local/bin/crypt4gh
$ podman run --it --rm --entrypoint /usr/local/bin/crypt4gh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crypt4gh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### crypt4gh-keygen

```bash
$ singularity exec <container> /usr/local/bin/crypt4gh-keygen
$ podman run --it --rm --entrypoint /usr/local/bin/crypt4gh-keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crypt4gh-keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grz-cli

```bash
$ singularity exec <container> /usr/local/bin/grz-cli
$ podman run --it --rm --entrypoint /usr/local/bin/grz-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grz-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### jp.py

```bash
$ singularity exec <container> /usr/local/bin/jp.py
$ podman run --it --rm --entrypoint /usr/local/bin/jp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonschema

```bash
$ singularity exec <container> /usr/local/bin/jsonschema
$ podman run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
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