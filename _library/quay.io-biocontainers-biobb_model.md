---
layout: container
name:  "quay.io/biocontainers/biobb_model"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biobb_model/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/biobb_model/container.yaml"
updated_at: "2025-12-16 04:10:41.481589"
latest: "5.1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/biobb_model"
aliases:
 - "check_structure"
 - "checking_log"
 - "fix_amides"
 - "fix_backbone"
 - "fix_chirality"
 - "fix_side_chain"
 - "mutate"
 - "normalizer"
 - "f2py3.10"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "3.8.0--pyhdfd78af_0"
 - "3.8.1--pyhdfd78af_0"
 - "3.9.0--pyhdfd78af_0"
 - "4.0.0--pyhdfd78af_0"
 - "4.0.1--pyhdfd78af_0"
 - "4.1.0--pyhdfd78af_0"
 - "4.2.1--pyhdfd78af_0"
 - "4.2.3--pyhdfd78af_0"
 - "5.0.0--pyhdfd78af_0"
 - "5.1.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for biobb_model"
config: {"url": "https://biocontainers.pro/tools/biobb_model", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for biobb_model", "latest": {"5.1.0--pyhdfd78af_0": "sha256:509ee086101cf4d0afa7545f82c170e98306b7b9eca9636ba44aa54d4e409697"}, "tags": {"3.8.0--pyhdfd78af_0": "sha256:b166cdac4abfb4d5e77ff3b74c587a381a42f8d798ab90a2abb5a99b99fa9ea1", "3.8.1--pyhdfd78af_0": "sha256:19b5815d31611fce680b84c10f11a4daf528d6263e8d23473754706b67445f44", "3.9.0--pyhdfd78af_0": "sha256:0e76e79054236535878bf22d408ea1fb7a59fdd49265c4707e48116cbf67e5aa", "4.0.0--pyhdfd78af_0": "sha256:1a1d7a5086ad6f49c828caa14fecf89a95d5c529e974f393551ec2f92406633c", "4.0.1--pyhdfd78af_0": "sha256:44f67be65e6a3d9d05771fd1660bffc52108ddbec9bf4e465c60bb39b05ff3df", "4.1.0--pyhdfd78af_0": "sha256:258fdb6613ea9f36bd832c7b50798954c943320373d4b839053635d48874bb32", "4.2.1--pyhdfd78af_0": "sha256:1f2f1efb7ccaaaa454c6197db0a6a113b3d75ade7bfcec2ce8ed38d09c2989df", "4.2.3--pyhdfd78af_0": "sha256:c853766d161b21b9111f5c7c191692f8a58cf320a9415908478d5bbd169db88b", "5.0.0--pyhdfd78af_0": "sha256:4267c758794f3b5dd4ab8a3d9618516d0bd1bc6ca5d1ef9d409aebae921b6aa8", "5.1.0--pyhdfd78af_0": "sha256:509ee086101cf4d0afa7545f82c170e98306b7b9eca9636ba44aa54d4e409697"}, "docker": "quay.io/biocontainers/biobb_model", "aliases": {"check_structure": "/usr/local/bin/check_structure", "checking_log": "/usr/local/bin/checking_log", "fix_amides": "/usr/local/bin/fix_amides", "fix_backbone": "/usr/local/bin/fix_backbone", "fix_chirality": "/usr/local/bin/fix_chirality", "fix_side_chain": "/usr/local/bin/fix_side_chain", "mutate": "/usr/local/bin/mutate", "normalizer": "/usr/local/bin/normalizer", "f2py3.10": "/usr/local/bin/f2py3.10", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biobb_model.
shpc-registry automated BioContainers addition for biobb_model
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biobb_model
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biobb_model:5.1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biobb_model/5.1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/biobb_model/5.1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biobb_model-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biobb_model-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biobb_model-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biobb_model-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biobb_model-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biobb_model-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### check_structure

```bash
$ singularity exec <container> /usr/local/bin/check_structure
$ podman run --it --rm --entrypoint /usr/local/bin/check_structure   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_structure   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checking_log

```bash
$ singularity exec <container> /usr/local/bin/checking_log
$ podman run --it --rm --entrypoint /usr/local/bin/checking_log   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checking_log   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fix_amides

```bash
$ singularity exec <container> /usr/local/bin/fix_amides
$ podman run --it --rm --entrypoint /usr/local/bin/fix_amides   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fix_amides   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fix_backbone

```bash
$ singularity exec <container> /usr/local/bin/fix_backbone
$ podman run --it --rm --entrypoint /usr/local/bin/fix_backbone   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fix_backbone   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fix_chirality

```bash
$ singularity exec <container> /usr/local/bin/fix_chirality
$ podman run --it --rm --entrypoint /usr/local/bin/fix_chirality   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fix_chirality   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fix_side_chain

```bash
$ singularity exec <container> /usr/local/bin/fix_side_chain
$ podman run --it --rm --entrypoint /usr/local/bin/fix_side_chain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fix_side_chain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mutate

```bash
$ singularity exec <container> /usr/local/bin/mutate
$ podman run --it --rm --entrypoint /usr/local/bin/mutate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mutate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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