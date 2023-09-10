---
layout: container
name:  "quay.io/biocontainers/latch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/latch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/latch/container.yaml"
updated_at: "2023-09-10 02:36:28.378344"
latest: "2.19.11--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/latch"
aliases:
 - "apython"
 - "aws"
 - "aws.cmd"
 - "aws_bash_completer"
 - "aws_completer"
 - "aws_zsh_completer.sh"
 - "cookiecutter"
 - "entrypoint.py"
 - "flyte-cli"
 - "flytekit_build_image.sh"
 - "flytekit_venv"
 - "gql-cli"
 - "keyring"
 - "latch"
 - "publish.py"
 - "pyflyte"
 - "pyflyte-execute"
 - "pyflyte-fast-execute"
 - "pyflyte-map-execute"
 - "slugify"
 - "watchfiles"
 - "wsdump"
 - "unidecode"
 - "csv-import"
 - "orc-memory"
 - "orc-scan"
 - "timezone-dump"
 - "plasma-store-server"
 - "plasma_store"
 - "sha256_profile"
 - "orc-contents"
 - "orc-metadata"
 - "orc-statistics"
 - "gflags_completions.sh"
 - "grpc_cpp_plugin"
 - "grpc_csharp_plugin"
 - "grpc_node_plugin"
 - "grpc_objective_c_plugin"
 - "grpc_php_plugin"
 - "grpc_python_plugin"
 - "grpc_ruby_plugin"
 - "jp.py"
 - "natsort"
 - "pyrsa-decrypt"
 - "pyrsa-encrypt"
 - "pyrsa-keygen"
 - "pyrsa-priv2pub"
versions:
 - "2.19.11--pyhdfd78af_0"
description: "singularity registry hpc automated addition for latch"
config: {"url": "https://biocontainers.pro/tools/latch", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for latch", "latest": {"2.19.11--pyhdfd78af_0": "sha256:439b0bf3495c40a02297b70a3c0d90e6b1d3b3120a5c727038abbc52653b27b4"}, "tags": {"2.19.11--pyhdfd78af_0": "sha256:439b0bf3495c40a02297b70a3c0d90e6b1d3b3120a5c727038abbc52653b27b4"}, "docker": "quay.io/biocontainers/latch", "aliases": {"apython": "/usr/local/bin/apython", "aws": "/usr/local/bin/aws", "aws.cmd": "/usr/local/bin/aws.cmd", "aws_bash_completer": "/usr/local/bin/aws_bash_completer", "aws_completer": "/usr/local/bin/aws_completer", "aws_zsh_completer.sh": "/usr/local/bin/aws_zsh_completer.sh", "cookiecutter": "/usr/local/bin/cookiecutter", "entrypoint.py": "/usr/local/bin/entrypoint.py", "flyte-cli": "/usr/local/bin/flyte-cli", "flytekit_build_image.sh": "/usr/local/bin/flytekit_build_image.sh", "flytekit_venv": "/usr/local/bin/flytekit_venv", "gql-cli": "/usr/local/bin/gql-cli", "keyring": "/usr/local/bin/keyring", "latch": "/usr/local/bin/latch", "publish.py": "/usr/local/bin/publish.py", "pyflyte": "/usr/local/bin/pyflyte", "pyflyte-execute": "/usr/local/bin/pyflyte-execute", "pyflyte-fast-execute": "/usr/local/bin/pyflyte-fast-execute", "pyflyte-map-execute": "/usr/local/bin/pyflyte-map-execute", "slugify": "/usr/local/bin/slugify", "watchfiles": "/usr/local/bin/watchfiles", "wsdump": "/usr/local/bin/wsdump", "unidecode": "/usr/local/bin/unidecode", "csv-import": "/usr/local/bin/csv-import", "orc-memory": "/usr/local/bin/orc-memory", "orc-scan": "/usr/local/bin/orc-scan", "timezone-dump": "/usr/local/bin/timezone-dump", "plasma-store-server": "/usr/local/bin/plasma-store-server", "plasma_store": "/usr/local/bin/plasma_store", "sha256_profile": "/usr/local/bin/sha256_profile", "orc-contents": "/usr/local/bin/orc-contents", "orc-metadata": "/usr/local/bin/orc-metadata", "orc-statistics": "/usr/local/bin/orc-statistics", "gflags_completions.sh": "/usr/local/bin/gflags_completions.sh", "grpc_cpp_plugin": "/usr/local/bin/grpc_cpp_plugin", "grpc_csharp_plugin": "/usr/local/bin/grpc_csharp_plugin", "grpc_node_plugin": "/usr/local/bin/grpc_node_plugin", "grpc_objective_c_plugin": "/usr/local/bin/grpc_objective_c_plugin", "grpc_php_plugin": "/usr/local/bin/grpc_php_plugin", "grpc_python_plugin": "/usr/local/bin/grpc_python_plugin", "grpc_ruby_plugin": "/usr/local/bin/grpc_ruby_plugin", "jp.py": "/usr/local/bin/jp.py", "natsort": "/usr/local/bin/natsort", "pyrsa-decrypt": "/usr/local/bin/pyrsa-decrypt", "pyrsa-encrypt": "/usr/local/bin/pyrsa-encrypt", "pyrsa-keygen": "/usr/local/bin/pyrsa-keygen", "pyrsa-priv2pub": "/usr/local/bin/pyrsa-priv2pub"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/latch.
singularity registry hpc automated addition for latch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/latch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/latch:2.19.11--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/latch/2.19.11--pyhdfd78af_0
$ module help quay.io/biocontainers/latch/2.19.11--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### latch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### latch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### latch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### latch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### latch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### latch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### apython

```bash
$ singularity exec <container> /usr/local/bin/apython
$ podman run --it --rm --entrypoint /usr/local/bin/apython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/apython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aws

```bash
$ singularity exec <container> /usr/local/bin/aws
$ podman run --it --rm --entrypoint /usr/local/bin/aws   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aws   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aws.cmd

```bash
$ singularity exec <container> /usr/local/bin/aws.cmd
$ podman run --it --rm --entrypoint /usr/local/bin/aws.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aws.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aws_bash_completer

```bash
$ singularity exec <container> /usr/local/bin/aws_bash_completer
$ podman run --it --rm --entrypoint /usr/local/bin/aws_bash_completer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aws_bash_completer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aws_completer

```bash
$ singularity exec <container> /usr/local/bin/aws_completer
$ podman run --it --rm --entrypoint /usr/local/bin/aws_completer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aws_completer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aws_zsh_completer.sh

```bash
$ singularity exec <container> /usr/local/bin/aws_zsh_completer.sh
$ podman run --it --rm --entrypoint /usr/local/bin/aws_zsh_completer.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aws_zsh_completer.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cookiecutter

```bash
$ singularity exec <container> /usr/local/bin/cookiecutter
$ podman run --it --rm --entrypoint /usr/local/bin/cookiecutter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cookiecutter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### entrypoint.py

```bash
$ singularity exec <container> /usr/local/bin/entrypoint.py
$ podman run --it --rm --entrypoint /usr/local/bin/entrypoint.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/entrypoint.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flyte-cli

```bash
$ singularity exec <container> /usr/local/bin/flyte-cli
$ podman run --it --rm --entrypoint /usr/local/bin/flyte-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flyte-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flytekit_build_image.sh

```bash
$ singularity exec <container> /usr/local/bin/flytekit_build_image.sh
$ podman run --it --rm --entrypoint /usr/local/bin/flytekit_build_image.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flytekit_build_image.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flytekit_venv

```bash
$ singularity exec <container> /usr/local/bin/flytekit_venv
$ podman run --it --rm --entrypoint /usr/local/bin/flytekit_venv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flytekit_venv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gql-cli

```bash
$ singularity exec <container> /usr/local/bin/gql-cli
$ podman run --it --rm --entrypoint /usr/local/bin/gql-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gql-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### keyring

```bash
$ singularity exec <container> /usr/local/bin/keyring
$ podman run --it --rm --entrypoint /usr/local/bin/keyring   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/keyring   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### latch

```bash
$ singularity exec <container> /usr/local/bin/latch
$ podman run --it --rm --entrypoint /usr/local/bin/latch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/latch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### publish.py

```bash
$ singularity exec <container> /usr/local/bin/publish.py
$ podman run --it --rm --entrypoint /usr/local/bin/publish.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/publish.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyflyte

```bash
$ singularity exec <container> /usr/local/bin/pyflyte
$ podman run --it --rm --entrypoint /usr/local/bin/pyflyte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyflyte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyflyte-execute

```bash
$ singularity exec <container> /usr/local/bin/pyflyte-execute
$ podman run --it --rm --entrypoint /usr/local/bin/pyflyte-execute   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyflyte-execute   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyflyte-fast-execute

```bash
$ singularity exec <container> /usr/local/bin/pyflyte-fast-execute
$ podman run --it --rm --entrypoint /usr/local/bin/pyflyte-fast-execute   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyflyte-fast-execute   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyflyte-map-execute

```bash
$ singularity exec <container> /usr/local/bin/pyflyte-map-execute
$ podman run --it --rm --entrypoint /usr/local/bin/pyflyte-map-execute   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyflyte-map-execute   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slugify

```bash
$ singularity exec <container> /usr/local/bin/slugify
$ podman run --it --rm --entrypoint /usr/local/bin/slugify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slugify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### watchfiles

```bash
$ singularity exec <container> /usr/local/bin/watchfiles
$ podman run --it --rm --entrypoint /usr/local/bin/watchfiles   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/watchfiles   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wsdump

```bash
$ singularity exec <container> /usr/local/bin/wsdump
$ podman run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unidecode

```bash
$ singularity exec <container> /usr/local/bin/unidecode
$ podman run --it --rm --entrypoint /usr/local/bin/unidecode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unidecode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csv-import

```bash
$ singularity exec <container> /usr/local/bin/csv-import
$ podman run --it --rm --entrypoint /usr/local/bin/csv-import   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csv-import   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-memory

```bash
$ singularity exec <container> /usr/local/bin/orc-memory
$ podman run --it --rm --entrypoint /usr/local/bin/orc-memory   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-memory   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-scan

```bash
$ singularity exec <container> /usr/local/bin/orc-scan
$ podman run --it --rm --entrypoint /usr/local/bin/orc-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### timezone-dump

```bash
$ singularity exec <container> /usr/local/bin/timezone-dump
$ podman run --it --rm --entrypoint /usr/local/bin/timezone-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/timezone-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plasma-store-server

```bash
$ singularity exec <container> /usr/local/bin/plasma-store-server
$ podman run --it --rm --entrypoint /usr/local/bin/plasma-store-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plasma-store-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plasma_store

```bash
$ singularity exec <container> /usr/local/bin/plasma_store
$ podman run --it --rm --entrypoint /usr/local/bin/plasma_store   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plasma_store   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sha256_profile

```bash
$ singularity exec <container> /usr/local/bin/sha256_profile
$ podman run --it --rm --entrypoint /usr/local/bin/sha256_profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sha256_profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-contents

```bash
$ singularity exec <container> /usr/local/bin/orc-contents
$ podman run --it --rm --entrypoint /usr/local/bin/orc-contents   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-contents   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-metadata

```bash
$ singularity exec <container> /usr/local/bin/orc-metadata
$ podman run --it --rm --entrypoint /usr/local/bin/orc-metadata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-metadata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-statistics

```bash
$ singularity exec <container> /usr/local/bin/orc-statistics
$ podman run --it --rm --entrypoint /usr/local/bin/orc-statistics   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-statistics   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gflags_completions.sh

```bash
$ singularity exec <container> /usr/local/bin/gflags_completions.sh
$ podman run --it --rm --entrypoint /usr/local/bin/gflags_completions.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gflags_completions.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_cpp_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_cpp_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_cpp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_cpp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_csharp_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_csharp_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_csharp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_csharp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_node_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_node_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_node_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_node_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_objective_c_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_objective_c_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_objective_c_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_objective_c_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_php_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_php_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_php_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_php_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_python_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_python_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_python_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_python_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_ruby_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_ruby_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_ruby_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_ruby_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jp.py

```bash
$ singularity exec <container> /usr/local/bin/jp.py
$ podman run --it --rm --entrypoint /usr/local/bin/jp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### natsort

```bash
$ singularity exec <container> /usr/local/bin/natsort
$ podman run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-decrypt

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-decrypt
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-decrypt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-decrypt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-encrypt

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-encrypt
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-encrypt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-encrypt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-keygen

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-keygen
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-priv2pub

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-priv2pub
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-priv2pub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-priv2pub   -v ${PWD} -w ${PWD} <container> -c " $@"
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