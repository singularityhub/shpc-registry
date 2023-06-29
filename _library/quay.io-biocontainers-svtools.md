---
layout: container
name:  "quay.io/biocontainers/svtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/svtools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/svtools/container.yaml"
updated_at: "2023-06-29 03:43:42.522233"
latest: "0.5.1--py_0"
container_url: "https://biocontainers.pro/tools/svtools"
aliases:
 - "create_coordinates"
 - "google_accounts_daemon"
 - "google_clock_skew_daemon"
 - "google_instance_setup"
 - "google_metadata_script_runner"
 - "google_network_daemon"
 - "google_optimize_local_ssd"
 - "google_set_multiqueue"
 - "lib_stats.R"
 - "sv_classifier.py"
 - "svtools"
 - "svtyper"
 - "svtyper-sso"
 - "update_info.py"
 - "vcf_allele_freq.py"
 - "vcf_group_multiline.py"
 - "vcf_modify_header.py"
 - "vcf_paste.py"
 - "pyrsa-decrypt-bigfile"
 - "pyrsa-encrypt-bigfile"
 - "asadmin"
 - "bundle_image"
 - "cfadmin"
 - "cq"
 - "cwutil"
 - "dynamodb_dump"
 - "dynamodb_load"
 - "elbadmin"
versions:
 - "0.5.1--py_0"
description: "shpc-registry automated BioContainers addition for svtools"
config: {"url": "https://biocontainers.pro/tools/svtools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for svtools", "latest": {"0.5.1--py_0": "sha256:6cb8fb48af0948c08d66375ff2a6bdb10eeaf88f2627a34bb32f59d041baf346"}, "tags": {"0.5.1--py_0": "sha256:6cb8fb48af0948c08d66375ff2a6bdb10eeaf88f2627a34bb32f59d041baf346"}, "docker": "quay.io/biocontainers/svtools", "aliases": {"create_coordinates": "/usr/local/bin/create_coordinates", "google_accounts_daemon": "/usr/local/bin/google_accounts_daemon", "google_clock_skew_daemon": "/usr/local/bin/google_clock_skew_daemon", "google_instance_setup": "/usr/local/bin/google_instance_setup", "google_metadata_script_runner": "/usr/local/bin/google_metadata_script_runner", "google_network_daemon": "/usr/local/bin/google_network_daemon", "google_optimize_local_ssd": "/usr/local/bin/google_optimize_local_ssd", "google_set_multiqueue": "/usr/local/bin/google_set_multiqueue", "lib_stats.R": "/usr/local/bin/lib_stats.R", "sv_classifier.py": "/usr/local/bin/sv_classifier.py", "svtools": "/usr/local/bin/svtools", "svtyper": "/usr/local/bin/svtyper", "svtyper-sso": "/usr/local/bin/svtyper-sso", "update_info.py": "/usr/local/bin/update_info.py", "vcf_allele_freq.py": "/usr/local/bin/vcf_allele_freq.py", "vcf_group_multiline.py": "/usr/local/bin/vcf_group_multiline.py", "vcf_modify_header.py": "/usr/local/bin/vcf_modify_header.py", "vcf_paste.py": "/usr/local/bin/vcf_paste.py", "pyrsa-decrypt-bigfile": "/usr/local/bin/pyrsa-decrypt-bigfile", "pyrsa-encrypt-bigfile": "/usr/local/bin/pyrsa-encrypt-bigfile", "asadmin": "/usr/local/bin/asadmin", "bundle_image": "/usr/local/bin/bundle_image", "cfadmin": "/usr/local/bin/cfadmin", "cq": "/usr/local/bin/cq", "cwutil": "/usr/local/bin/cwutil", "dynamodb_dump": "/usr/local/bin/dynamodb_dump", "dynamodb_load": "/usr/local/bin/dynamodb_load", "elbadmin": "/usr/local/bin/elbadmin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/svtools.
shpc-registry automated BioContainers addition for svtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/svtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/svtools:0.5.1--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/svtools/0.5.1--py_0
$ module help quay.io/biocontainers/svtools/0.5.1--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### svtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### svtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### svtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### svtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### svtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### svtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### create_coordinates

```bash
$ singularity exec <container> /usr/local/bin/create_coordinates
$ podman run --it --rm --entrypoint /usr/local/bin/create_coordinates   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_coordinates   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### google_accounts_daemon

```bash
$ singularity exec <container> /usr/local/bin/google_accounts_daemon
$ podman run --it --rm --entrypoint /usr/local/bin/google_accounts_daemon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/google_accounts_daemon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### google_clock_skew_daemon

```bash
$ singularity exec <container> /usr/local/bin/google_clock_skew_daemon
$ podman run --it --rm --entrypoint /usr/local/bin/google_clock_skew_daemon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/google_clock_skew_daemon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### google_instance_setup

```bash
$ singularity exec <container> /usr/local/bin/google_instance_setup
$ podman run --it --rm --entrypoint /usr/local/bin/google_instance_setup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/google_instance_setup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### google_metadata_script_runner

```bash
$ singularity exec <container> /usr/local/bin/google_metadata_script_runner
$ podman run --it --rm --entrypoint /usr/local/bin/google_metadata_script_runner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/google_metadata_script_runner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### google_network_daemon

```bash
$ singularity exec <container> /usr/local/bin/google_network_daemon
$ podman run --it --rm --entrypoint /usr/local/bin/google_network_daemon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/google_network_daemon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### google_optimize_local_ssd

```bash
$ singularity exec <container> /usr/local/bin/google_optimize_local_ssd
$ podman run --it --rm --entrypoint /usr/local/bin/google_optimize_local_ssd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/google_optimize_local_ssd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### google_set_multiqueue

```bash
$ singularity exec <container> /usr/local/bin/google_set_multiqueue
$ podman run --it --rm --entrypoint /usr/local/bin/google_set_multiqueue   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/google_set_multiqueue   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lib_stats.R

```bash
$ singularity exec <container> /usr/local/bin/lib_stats.R
$ podman run --it --rm --entrypoint /usr/local/bin/lib_stats.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lib_stats.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sv_classifier.py

```bash
$ singularity exec <container> /usr/local/bin/sv_classifier.py
$ podman run --it --rm --entrypoint /usr/local/bin/sv_classifier.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sv_classifier.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svtools

```bash
$ singularity exec <container> /usr/local/bin/svtools
$ podman run --it --rm --entrypoint /usr/local/bin/svtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svtyper

```bash
$ singularity exec <container> /usr/local/bin/svtyper
$ podman run --it --rm --entrypoint /usr/local/bin/svtyper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svtyper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svtyper-sso

```bash
$ singularity exec <container> /usr/local/bin/svtyper-sso
$ podman run --it --rm --entrypoint /usr/local/bin/svtyper-sso   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svtyper-sso   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### update_info.py

```bash
$ singularity exec <container> /usr/local/bin/update_info.py
$ podman run --it --rm --entrypoint /usr/local/bin/update_info.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/update_info.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_allele_freq.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_allele_freq.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_allele_freq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_allele_freq.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_group_multiline.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_group_multiline.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_group_multiline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_group_multiline.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_modify_header.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_modify_header.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_modify_header.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_modify_header.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcf_paste.py

```bash
$ singularity exec <container> /usr/local/bin/vcf_paste.py
$ podman run --it --rm --entrypoint /usr/local/bin/vcf_paste.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf_paste.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-decrypt-bigfile

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-decrypt-bigfile
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-decrypt-bigfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-decrypt-bigfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-encrypt-bigfile

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-encrypt-bigfile
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-encrypt-bigfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-encrypt-bigfile   -v ${PWD} -w ${PWD} <container> -c " $@"
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