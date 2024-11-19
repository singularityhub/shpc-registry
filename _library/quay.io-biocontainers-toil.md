---
layout: container
name:  "quay.io/biocontainers/toil"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/toil/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/toil/container.yaml"
updated_at: "2024-11-19 03:22:04.688390"
latest: "7.0.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/toil"
aliases:
 - "_toil_contained_executor"
 - "_toil_mesos_executor"
 - "_toil_worker"
 - "bagit.py"
 - "black"
 - "black-primer"
 - "blackd"
 - "cwltoil"
 - "galaxy-tool-test"
 - "mulled-build"
 - "mulled-build-channel"
 - "mulled-build-files"
 - "mulled-build-tool"
 - "mulled-search"
 - "prov-compare"
 - "prov-convert"
 - "toil"
 - "toil-cwl-runner"
 - "wsdump"
 - "cwltool"
 - "schema-salad-doc"
 - "schema-salad-tool"
 - "asadmin"
 - "bundle_image"
 - "cfadmin"
 - "cq"
 - "csv2rdf"
 - "cwutil"
 - "dynamodb_dump"
versions:
 - "5.6.0--pyhdfd78af_0"
 - "5.7.1--pyhdfd78af_0"
 - "5.9.2--pyhdfd78af_0"
 - "5.11.0--pyhdfd78af_0"
 - "5.12.0--pyhdfd78af_0"
 - "6.0.0--pyhdfd78af_0"
 - "6.1.0--pyhdfd78af_0"
 - "7.0.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for toil"
config: {"url": "https://biocontainers.pro/tools/toil", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for toil", "latest": {"7.0.0--pyhdfd78af_0": "sha256:85232a4feb6a033224cdc51621dad9f3db772fead22c8d03726bcb7010152f92"}, "tags": {"5.6.0--pyhdfd78af_0": "sha256:d148c547f7829b59b69155dd5add29ddd2d8a3b93e10f3f9ebbdb1126bc63041", "5.7.1--pyhdfd78af_0": "sha256:7357d1c1b2a28d5bd40358196d92dcc83495d7f54864335dec14b14c31764dec", "5.9.2--pyhdfd78af_0": "sha256:eb52b735ebfd4476ebc0fb109ca6568c029003841aeb9a7d729390f96a53f7b5", "5.11.0--pyhdfd78af_0": "sha256:4dcd3fc2c667eab6f09756d85bf9ae1753dddef532394047176f31f5cfbcf497", "5.12.0--pyhdfd78af_0": "sha256:92f5fda499b086f595ac35727d61655983ff77835a7ff78bd27e973f0e97ec68", "6.0.0--pyhdfd78af_0": "sha256:3a1b9f73af7765708c15ed1e750bdf9a08617d0e8dbff037ca25ac39066ff524", "6.1.0--pyhdfd78af_0": "sha256:3b4f9201153ccc6073dda92b70245ab579ed5da74c97bfda4e61bce30a41a503", "7.0.0--pyhdfd78af_0": "sha256:85232a4feb6a033224cdc51621dad9f3db772fead22c8d03726bcb7010152f92"}, "docker": "quay.io/biocontainers/toil", "aliases": {"_toil_contained_executor": "/usr/local/bin/_toil_contained_executor", "_toil_mesos_executor": "/usr/local/bin/_toil_mesos_executor", "_toil_worker": "/usr/local/bin/_toil_worker", "bagit.py": "/usr/local/bin/bagit.py", "black": "/usr/local/bin/black", "black-primer": "/usr/local/bin/black-primer", "blackd": "/usr/local/bin/blackd", "cwltoil": "/usr/local/bin/cwltoil", "galaxy-tool-test": "/usr/local/bin/galaxy-tool-test", "mulled-build": "/usr/local/bin/mulled-build", "mulled-build-channel": "/usr/local/bin/mulled-build-channel", "mulled-build-files": "/usr/local/bin/mulled-build-files", "mulled-build-tool": "/usr/local/bin/mulled-build-tool", "mulled-search": "/usr/local/bin/mulled-search", "prov-compare": "/usr/local/bin/prov-compare", "prov-convert": "/usr/local/bin/prov-convert", "toil": "/usr/local/bin/toil", "toil-cwl-runner": "/usr/local/bin/toil-cwl-runner", "wsdump": "/usr/local/bin/wsdump", "cwltool": "/usr/local/bin/cwltool", "schema-salad-doc": "/usr/local/bin/schema-salad-doc", "schema-salad-tool": "/usr/local/bin/schema-salad-tool", "asadmin": "/usr/local/bin/asadmin", "bundle_image": "/usr/local/bin/bundle_image", "cfadmin": "/usr/local/bin/cfadmin", "cq": "/usr/local/bin/cq", "csv2rdf": "/usr/local/bin/csv2rdf", "cwutil": "/usr/local/bin/cwutil", "dynamodb_dump": "/usr/local/bin/dynamodb_dump"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/toil.
shpc-registry automated BioContainers addition for toil
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/toil
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/toil:7.0.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/toil/7.0.0--pyhdfd78af_0
$ module help quay.io/biocontainers/toil/7.0.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### toil-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### toil-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### toil-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### toil-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### toil-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### toil-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### _toil_contained_executor

```bash
$ singularity exec <container> /usr/local/bin/_toil_contained_executor
$ podman run --it --rm --entrypoint /usr/local/bin/_toil_contained_executor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_toil_contained_executor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _toil_mesos_executor

```bash
$ singularity exec <container> /usr/local/bin/_toil_mesos_executor
$ podman run --it --rm --entrypoint /usr/local/bin/_toil_mesos_executor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_toil_mesos_executor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _toil_worker

```bash
$ singularity exec <container> /usr/local/bin/_toil_worker
$ podman run --it --rm --entrypoint /usr/local/bin/_toil_worker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_toil_worker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bagit.py

```bash
$ singularity exec <container> /usr/local/bin/bagit.py
$ podman run --it --rm --entrypoint /usr/local/bin/bagit.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bagit.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### black

```bash
$ singularity exec <container> /usr/local/bin/black
$ podman run --it --rm --entrypoint /usr/local/bin/black   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/black   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### black-primer

```bash
$ singularity exec <container> /usr/local/bin/black-primer
$ podman run --it --rm --entrypoint /usr/local/bin/black-primer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/black-primer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blackd

```bash
$ singularity exec <container> /usr/local/bin/blackd
$ podman run --it --rm --entrypoint /usr/local/bin/blackd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blackd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwltoil

```bash
$ singularity exec <container> /usr/local/bin/cwltoil
$ podman run --it --rm --entrypoint /usr/local/bin/cwltoil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwltoil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### galaxy-tool-test

```bash
$ singularity exec <container> /usr/local/bin/galaxy-tool-test
$ podman run --it --rm --entrypoint /usr/local/bin/galaxy-tool-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/galaxy-tool-test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-build

```bash
$ singularity exec <container> /usr/local/bin/mulled-build
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-build-channel

```bash
$ singularity exec <container> /usr/local/bin/mulled-build-channel
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-build-channel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-build-channel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-build-files

```bash
$ singularity exec <container> /usr/local/bin/mulled-build-files
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-build-files   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-build-files   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-build-tool

```bash
$ singularity exec <container> /usr/local/bin/mulled-build-tool
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-build-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-build-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mulled-search

```bash
$ singularity exec <container> /usr/local/bin/mulled-search
$ podman run --it --rm --entrypoint /usr/local/bin/mulled-search   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mulled-search   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prov-compare

```bash
$ singularity exec <container> /usr/local/bin/prov-compare
$ podman run --it --rm --entrypoint /usr/local/bin/prov-compare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prov-compare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prov-convert

```bash
$ singularity exec <container> /usr/local/bin/prov-convert
$ podman run --it --rm --entrypoint /usr/local/bin/prov-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prov-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### toil

```bash
$ singularity exec <container> /usr/local/bin/toil
$ podman run --it --rm --entrypoint /usr/local/bin/toil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/toil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### toil-cwl-runner

```bash
$ singularity exec <container> /usr/local/bin/toil-cwl-runner
$ podman run --it --rm --entrypoint /usr/local/bin/toil-cwl-runner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/toil-cwl-runner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wsdump

```bash
$ singularity exec <container> /usr/local/bin/wsdump
$ podman run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwltool

```bash
$ singularity exec <container> /usr/local/bin/cwltool
$ podman run --it --rm --entrypoint /usr/local/bin/cwltool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwltool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### schema-salad-doc

```bash
$ singularity exec <container> /usr/local/bin/schema-salad-doc
$ podman run --it --rm --entrypoint /usr/local/bin/schema-salad-doc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/schema-salad-doc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### schema-salad-tool

```bash
$ singularity exec <container> /usr/local/bin/schema-salad-tool
$ podman run --it --rm --entrypoint /usr/local/bin/schema-salad-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/schema-salad-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asadmin

```bash
$ singularity exec <container> /usr/local/bin/asadmin
$ podman run --it --rm --entrypoint /usr/local/bin/asadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bundle_image

```bash
$ singularity exec <container> /usr/local/bin/bundle_image
$ podman run --it --rm --entrypoint /usr/local/bin/bundle_image   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bundle_image   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cfadmin

```bash
$ singularity exec <container> /usr/local/bin/cfadmin
$ podman run --it --rm --entrypoint /usr/local/bin/cfadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cfadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cq

```bash
$ singularity exec <container> /usr/local/bin/cq
$ podman run --it --rm --entrypoint /usr/local/bin/cq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csv2rdf

```bash
$ singularity exec <container> /usr/local/bin/csv2rdf
$ podman run --it --rm --entrypoint /usr/local/bin/csv2rdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csv2rdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwutil

```bash
$ singularity exec <container> /usr/local/bin/cwutil
$ podman run --it --rm --entrypoint /usr/local/bin/cwutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dynamodb_dump

```bash
$ singularity exec <container> /usr/local/bin/dynamodb_dump
$ podman run --it --rm --entrypoint /usr/local/bin/dynamodb_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dynamodb_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
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