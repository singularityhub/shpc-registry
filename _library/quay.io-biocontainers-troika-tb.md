---
layout: container
name:  "quay.io/biocontainers/troika-tb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/troika-tb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/troika-tb/container.yaml"
updated_at: "2024-08-25 03:04:24.157877"
latest: "0.0.5--py_0"
container_url: "https://biocontainers.pro/tools/troika-tb"
aliases:
 - "troika"
 - "asadmin"
 - "bundle_image"
 - "cfadmin"
 - "cq"
 - "cwutil"
 - "dynamodb_dump"
 - "dynamodb_load"
 - "elbadmin"
 - "fetch_file"
 - "glacier"
 - "instance_events"
 - "kill_instance"
 - "launch_instance"
 - "list_instances"
 - "lss3"
 - "mturk"
 - "pyami_sendmail"
 - "route53"
 - "s3put"
 - "sdbadmin"
 - "taskadmin"
 - "vba_extract.py"
 - "pulptest"
 - "cbc"
 - "clp"
versions:
 - "0.0.5--py_0"
description: "singularity registry hpc automated addition for troika-tb"
config: {"url": "https://biocontainers.pro/tools/troika-tb", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for troika-tb", "latest": {"0.0.5--py_0": "sha256:5497520cfce9accbeb2d86f5b5d8172b59475cf6fb0fc1009793be4051cb4b2b"}, "tags": {"0.0.5--py_0": "sha256:5497520cfce9accbeb2d86f5b5d8172b59475cf6fb0fc1009793be4051cb4b2b"}, "docker": "quay.io/biocontainers/troika-tb", "aliases": {"troika": "/usr/local/bin/troika", "asadmin": "/usr/local/bin/asadmin", "bundle_image": "/usr/local/bin/bundle_image", "cfadmin": "/usr/local/bin/cfadmin", "cq": "/usr/local/bin/cq", "cwutil": "/usr/local/bin/cwutil", "dynamodb_dump": "/usr/local/bin/dynamodb_dump", "dynamodb_load": "/usr/local/bin/dynamodb_load", "elbadmin": "/usr/local/bin/elbadmin", "fetch_file": "/usr/local/bin/fetch_file", "glacier": "/usr/local/bin/glacier", "instance_events": "/usr/local/bin/instance_events", "kill_instance": "/usr/local/bin/kill_instance", "launch_instance": "/usr/local/bin/launch_instance", "list_instances": "/usr/local/bin/list_instances", "lss3": "/usr/local/bin/lss3", "mturk": "/usr/local/bin/mturk", "pyami_sendmail": "/usr/local/bin/pyami_sendmail", "route53": "/usr/local/bin/route53", "s3put": "/usr/local/bin/s3put", "sdbadmin": "/usr/local/bin/sdbadmin", "taskadmin": "/usr/local/bin/taskadmin", "vba_extract.py": "/usr/local/bin/vba_extract.py", "pulptest": "/usr/local/bin/pulptest", "cbc": "/usr/local/bin/cbc", "clp": "/usr/local/bin/clp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/troika-tb.
singularity registry hpc automated addition for troika-tb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/troika-tb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/troika-tb:0.0.5--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/troika-tb/0.0.5--py_0
$ module help quay.io/biocontainers/troika-tb/0.0.5--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### troika-tb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### troika-tb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### troika-tb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### troika-tb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### troika-tb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### troika-tb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### troika

```bash
$ singularity exec <container> /usr/local/bin/troika
$ podman run --it --rm --entrypoint /usr/local/bin/troika   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/troika   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### dynamodb_load

```bash
$ singularity exec <container> /usr/local/bin/dynamodb_load
$ podman run --it --rm --entrypoint /usr/local/bin/dynamodb_load   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dynamodb_load   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elbadmin

```bash
$ singularity exec <container> /usr/local/bin/elbadmin
$ podman run --it --rm --entrypoint /usr/local/bin/elbadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elbadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch_file

```bash
$ singularity exec <container> /usr/local/bin/fetch_file
$ podman run --it --rm --entrypoint /usr/local/bin/fetch_file   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch_file   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glacier

```bash
$ singularity exec <container> /usr/local/bin/glacier
$ podman run --it --rm --entrypoint /usr/local/bin/glacier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glacier   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### instance_events

```bash
$ singularity exec <container> /usr/local/bin/instance_events
$ podman run --it --rm --entrypoint /usr/local/bin/instance_events   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/instance_events   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kill_instance

```bash
$ singularity exec <container> /usr/local/bin/kill_instance
$ podman run --it --rm --entrypoint /usr/local/bin/kill_instance   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kill_instance   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### launch_instance

```bash
$ singularity exec <container> /usr/local/bin/launch_instance
$ podman run --it --rm --entrypoint /usr/local/bin/launch_instance   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/launch_instance   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### list_instances

```bash
$ singularity exec <container> /usr/local/bin/list_instances
$ podman run --it --rm --entrypoint /usr/local/bin/list_instances   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/list_instances   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lss3

```bash
$ singularity exec <container> /usr/local/bin/lss3
$ podman run --it --rm --entrypoint /usr/local/bin/lss3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lss3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mturk

```bash
$ singularity exec <container> /usr/local/bin/mturk
$ podman run --it --rm --entrypoint /usr/local/bin/mturk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mturk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyami_sendmail

```bash
$ singularity exec <container> /usr/local/bin/pyami_sendmail
$ podman run --it --rm --entrypoint /usr/local/bin/pyami_sendmail   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyami_sendmail   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### route53

```bash
$ singularity exec <container> /usr/local/bin/route53
$ podman run --it --rm --entrypoint /usr/local/bin/route53   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/route53   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### s3put

```bash
$ singularity exec <container> /usr/local/bin/s3put
$ podman run --it --rm --entrypoint /usr/local/bin/s3put   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/s3put   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdbadmin

```bash
$ singularity exec <container> /usr/local/bin/sdbadmin
$ podman run --it --rm --entrypoint /usr/local/bin/sdbadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdbadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taskadmin

```bash
$ singularity exec <container> /usr/local/bin/taskadmin
$ podman run --it --rm --entrypoint /usr/local/bin/taskadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taskadmin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vba_extract.py

```bash
$ singularity exec <container> /usr/local/bin/vba_extract.py
$ podman run --it --rm --entrypoint /usr/local/bin/vba_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vba_extract.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pulptest

```bash
$ singularity exec <container> /usr/local/bin/pulptest
$ podman run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pulptest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbc

```bash
$ singularity exec <container> /usr/local/bin/cbc
$ podman run --it --rm --entrypoint /usr/local/bin/cbc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clp

```bash
$ singularity exec <container> /usr/local/bin/clp
$ podman run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
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