---
layout: container
name:  "quay.io/biocontainers/beacon2-import"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/beacon2-import/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/beacon2-import/container.yaml"
updated_at: "2026-01-03 03:35:49.175847"
latest: "2.2.4--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/beacon2-import"
aliases:
 - "beacon2-import"
 - "beacon2-search"
 - "bioblend-galaxy-tests"
 - "asadmin"
 - "bundle_image"
 - "cfadmin"
 - "cq"
 - "cwutil"
 - "cyvcf2"
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
 - "coloredlogs"
 - "humanfriendly"
 - "f2py3.6"
versions:
 - "1.0.6--pyhdfd78af_0"
 - "1.0.7--pyh7cba7a3_0"
 - "1.0.8--pyh7cba7a3_0"
 - "2.2.1--pyhdfd78af_0"
 - "2.1.0--pyhdfd78af_0"
 - "2.0.0--pyhdfd78af_0"
 - "2.2.3--pyhdfd78af_0"
 - "2.2.4--pyhdfd78af_0"
description: "singularity registry hpc automated addition for beacon2-import"
config: {"url": "https://biocontainers.pro/tools/beacon2-import", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for beacon2-import", "latest": {"2.2.4--pyhdfd78af_0": "sha256:86a97927de75bceea6952fb4b105cc7970f3d8cbc7e9606bffee4daf4e688c41"}, "tags": {"1.0.6--pyhdfd78af_0": "sha256:5ff5d5a1d915956323cd54ae7d8899f9c7fd2fce26da7194f9f0c1a37e129595", "1.0.7--pyh7cba7a3_0": "sha256:a019c442c47fdb6d566eb33dd02a33a12e639ffb3d35f59a06422a3e62504472", "1.0.8--pyh7cba7a3_0": "sha256:d3c6d43880476c24e00fc0b062563e4f6d6ae85cedecac5a5ceb07d592cc6e52", "2.2.1--pyhdfd78af_0": "sha256:321e3f31c54cea0f2882f23058356dc828b0281c2004bee655b21028edba842d", "2.1.0--pyhdfd78af_0": "sha256:97209869a1e4ef981640c596485d60595b6ea833af82f4e3070ae8a8843df56d", "2.0.0--pyhdfd78af_0": "sha256:1152e87eadb6af4f3f2a97705bf30d40c2d680a344d07b7b44dcc7fbb7ff8c44", "2.2.3--pyhdfd78af_0": "sha256:0440017d8c0d98043428a3d6b1fef81ad5cb38ed8c5b11e8b2a25d6dfadfc9db", "2.2.4--pyhdfd78af_0": "sha256:86a97927de75bceea6952fb4b105cc7970f3d8cbc7e9606bffee4daf4e688c41"}, "docker": "quay.io/biocontainers/beacon2-import", "aliases": {"beacon2-import": "/usr/local/bin/beacon2-import", "beacon2-search": "/usr/local/bin/beacon2-search", "bioblend-galaxy-tests": "/usr/local/bin/bioblend-galaxy-tests", "asadmin": "/usr/local/bin/asadmin", "bundle_image": "/usr/local/bin/bundle_image", "cfadmin": "/usr/local/bin/cfadmin", "cq": "/usr/local/bin/cq", "cwutil": "/usr/local/bin/cwutil", "cyvcf2": "/usr/local/bin/cyvcf2", "dynamodb_dump": "/usr/local/bin/dynamodb_dump", "dynamodb_load": "/usr/local/bin/dynamodb_load", "elbadmin": "/usr/local/bin/elbadmin", "fetch_file": "/usr/local/bin/fetch_file", "glacier": "/usr/local/bin/glacier", "instance_events": "/usr/local/bin/instance_events", "kill_instance": "/usr/local/bin/kill_instance", "launch_instance": "/usr/local/bin/launch_instance", "list_instances": "/usr/local/bin/list_instances", "lss3": "/usr/local/bin/lss3", "mturk": "/usr/local/bin/mturk", "pyami_sendmail": "/usr/local/bin/pyami_sendmail", "route53": "/usr/local/bin/route53", "s3put": "/usr/local/bin/s3put", "sdbadmin": "/usr/local/bin/sdbadmin", "taskadmin": "/usr/local/bin/taskadmin", "coloredlogs": "/usr/local/bin/coloredlogs", "humanfriendly": "/usr/local/bin/humanfriendly", "f2py3.6": "/usr/local/bin/f2py3.6"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/beacon2-import.
singularity registry hpc automated addition for beacon2-import
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/beacon2-import
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/beacon2-import:2.2.4--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/beacon2-import/2.2.4--pyhdfd78af_0
$ module help quay.io/biocontainers/beacon2-import/2.2.4--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### beacon2-import-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### beacon2-import-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### beacon2-import-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### beacon2-import-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### beacon2-import-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### beacon2-import-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### beacon2-import

```bash
$ singularity exec <container> /usr/local/bin/beacon2-import
$ podman run --it --rm --entrypoint /usr/local/bin/beacon2-import   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/beacon2-import   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### beacon2-search

```bash
$ singularity exec <container> /usr/local/bin/beacon2-search
$ podman run --it --rm --entrypoint /usr/local/bin/beacon2-search   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/beacon2-search   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bioblend-galaxy-tests

```bash
$ singularity exec <container> /usr/local/bin/bioblend-galaxy-tests
$ podman run --it --rm --entrypoint /usr/local/bin/bioblend-galaxy-tests   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bioblend-galaxy-tests   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### cyvcf2

```bash
$ singularity exec <container> /usr/local/bin/cyvcf2
$ podman run --it --rm --entrypoint /usr/local/bin/cyvcf2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cyvcf2   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### coloredlogs

```bash
$ singularity exec <container> /usr/local/bin/coloredlogs
$ podman run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humanfriendly

```bash
$ singularity exec <container> /usr/local/bin/humanfriendly
$ podman run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.6

```bash
$ singularity exec <container> /usr/local/bin/f2py3.6
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
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