---
layout: container
name:  "quay.io/biocontainers/dxpy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dxpy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dxpy/container.yaml"
updated_at: "2023-07-30 03:13:02.284651"
latest: "0.318.1--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/dxpy"
aliases:
 - "dx"
 - "dx-app-wizard"
 - "dx-build-app"
 - "dx-build-applet"
 - "dx-clone-asset"
 - "dx-docker"
 - "dx-download-all-inputs"
 - "dx-fetch-bundled-depends"
 - "dx-generate-dxapp"
 - "dx-jobutil-add-output"
 - "dx-jobutil-dxlink"
 - "dx-jobutil-new-job"
 - "dx-jobutil-parse-link"
 - "dx-jobutil-report-error"
 - "dx-log-stream"
 - "dx-mount-all-inputs"
 - "dx-notebook-reconnect"
 - "dx-print-bash-vars"
 - "dx-upload-all-outputs"
 - "wsdump"
 - "xattr"
 - "activate-global-python-argcomplete"
 - "python-argcomplete-check-easy-install-script"
 - "python-argcomplete-tcsh"
 - "register-python-argcomplete"
 - "chardetect"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
 - "python3.8"
 - "python3.8-config"
versions:
 - "0.318.1--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for dxpy"
config: {"url": "https://biocontainers.pro/tools/dxpy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dxpy", "latest": {"0.318.1--pyh5e36f6f_0": "sha256:ab2f23ef517b0b0362c71bb36572dec96744eb3c5bb912fe91b369907e7ac3ca"}, "tags": {"0.318.1--pyh5e36f6f_0": "sha256:ab2f23ef517b0b0362c71bb36572dec96744eb3c5bb912fe91b369907e7ac3ca"}, "docker": "quay.io/biocontainers/dxpy", "aliases": {"dx": "/usr/local/bin/dx", "dx-app-wizard": "/usr/local/bin/dx-app-wizard", "dx-build-app": "/usr/local/bin/dx-build-app", "dx-build-applet": "/usr/local/bin/dx-build-applet", "dx-clone-asset": "/usr/local/bin/dx-clone-asset", "dx-docker": "/usr/local/bin/dx-docker", "dx-download-all-inputs": "/usr/local/bin/dx-download-all-inputs", "dx-fetch-bundled-depends": "/usr/local/bin/dx-fetch-bundled-depends", "dx-generate-dxapp": "/usr/local/bin/dx-generate-dxapp", "dx-jobutil-add-output": "/usr/local/bin/dx-jobutil-add-output", "dx-jobutil-dxlink": "/usr/local/bin/dx-jobutil-dxlink", "dx-jobutil-new-job": "/usr/local/bin/dx-jobutil-new-job", "dx-jobutil-parse-link": "/usr/local/bin/dx-jobutil-parse-link", "dx-jobutil-report-error": "/usr/local/bin/dx-jobutil-report-error", "dx-log-stream": "/usr/local/bin/dx-log-stream", "dx-mount-all-inputs": "/usr/local/bin/dx-mount-all-inputs", "dx-notebook-reconnect": "/usr/local/bin/dx-notebook-reconnect", "dx-print-bash-vars": "/usr/local/bin/dx-print-bash-vars", "dx-upload-all-outputs": "/usr/local/bin/dx-upload-all-outputs", "wsdump": "/usr/local/bin/wsdump", "xattr": "/usr/local/bin/xattr", "activate-global-python-argcomplete": "/usr/local/bin/activate-global-python-argcomplete", "python-argcomplete-check-easy-install-script": "/usr/local/bin/python-argcomplete-check-easy-install-script", "python-argcomplete-tcsh": "/usr/local/bin/python-argcomplete-tcsh", "register-python-argcomplete": "/usr/local/bin/register-python-argcomplete", "chardetect": "/usr/local/bin/chardetect", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8", "python3.8": "/usr/local/bin/python3.8", "python3.8-config": "/usr/local/bin/python3.8-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dxpy.
shpc-registry automated BioContainers addition for dxpy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dxpy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dxpy:0.318.1--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dxpy/0.318.1--pyh5e36f6f_0
$ module help quay.io/biocontainers/dxpy/0.318.1--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dxpy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dxpy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dxpy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dxpy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dxpy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dxpy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dx

```bash
$ singularity exec <container> /usr/local/bin/dx
$ podman run --it --rm --entrypoint /usr/local/bin/dx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-app-wizard

```bash
$ singularity exec <container> /usr/local/bin/dx-app-wizard
$ podman run --it --rm --entrypoint /usr/local/bin/dx-app-wizard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-app-wizard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-build-app

```bash
$ singularity exec <container> /usr/local/bin/dx-build-app
$ podman run --it --rm --entrypoint /usr/local/bin/dx-build-app   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-build-app   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-build-applet

```bash
$ singularity exec <container> /usr/local/bin/dx-build-applet
$ podman run --it --rm --entrypoint /usr/local/bin/dx-build-applet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-build-applet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-clone-asset

```bash
$ singularity exec <container> /usr/local/bin/dx-clone-asset
$ podman run --it --rm --entrypoint /usr/local/bin/dx-clone-asset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-clone-asset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-docker

```bash
$ singularity exec <container> /usr/local/bin/dx-docker
$ podman run --it --rm --entrypoint /usr/local/bin/dx-docker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-docker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-download-all-inputs

```bash
$ singularity exec <container> /usr/local/bin/dx-download-all-inputs
$ podman run --it --rm --entrypoint /usr/local/bin/dx-download-all-inputs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-download-all-inputs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-fetch-bundled-depends

```bash
$ singularity exec <container> /usr/local/bin/dx-fetch-bundled-depends
$ podman run --it --rm --entrypoint /usr/local/bin/dx-fetch-bundled-depends   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-fetch-bundled-depends   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-generate-dxapp

```bash
$ singularity exec <container> /usr/local/bin/dx-generate-dxapp
$ podman run --it --rm --entrypoint /usr/local/bin/dx-generate-dxapp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-generate-dxapp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-jobutil-add-output

```bash
$ singularity exec <container> /usr/local/bin/dx-jobutil-add-output
$ podman run --it --rm --entrypoint /usr/local/bin/dx-jobutil-add-output   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-jobutil-add-output   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-jobutil-dxlink

```bash
$ singularity exec <container> /usr/local/bin/dx-jobutil-dxlink
$ podman run --it --rm --entrypoint /usr/local/bin/dx-jobutil-dxlink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-jobutil-dxlink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-jobutil-new-job

```bash
$ singularity exec <container> /usr/local/bin/dx-jobutil-new-job
$ podman run --it --rm --entrypoint /usr/local/bin/dx-jobutil-new-job   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-jobutil-new-job   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-jobutil-parse-link

```bash
$ singularity exec <container> /usr/local/bin/dx-jobutil-parse-link
$ podman run --it --rm --entrypoint /usr/local/bin/dx-jobutil-parse-link   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-jobutil-parse-link   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-jobutil-report-error

```bash
$ singularity exec <container> /usr/local/bin/dx-jobutil-report-error
$ podman run --it --rm --entrypoint /usr/local/bin/dx-jobutil-report-error   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-jobutil-report-error   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-log-stream

```bash
$ singularity exec <container> /usr/local/bin/dx-log-stream
$ podman run --it --rm --entrypoint /usr/local/bin/dx-log-stream   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-log-stream   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-mount-all-inputs

```bash
$ singularity exec <container> /usr/local/bin/dx-mount-all-inputs
$ podman run --it --rm --entrypoint /usr/local/bin/dx-mount-all-inputs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-mount-all-inputs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-notebook-reconnect

```bash
$ singularity exec <container> /usr/local/bin/dx-notebook-reconnect
$ podman run --it --rm --entrypoint /usr/local/bin/dx-notebook-reconnect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-notebook-reconnect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-print-bash-vars

```bash
$ singularity exec <container> /usr/local/bin/dx-print-bash-vars
$ podman run --it --rm --entrypoint /usr/local/bin/dx-print-bash-vars   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-print-bash-vars   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dx-upload-all-outputs

```bash
$ singularity exec <container> /usr/local/bin/dx-upload-all-outputs
$ podman run --it --rm --entrypoint /usr/local/bin/dx-upload-all-outputs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dx-upload-all-outputs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wsdump

```bash
$ singularity exec <container> /usr/local/bin/wsdump
$ podman run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xattr

```bash
$ singularity exec <container> /usr/local/bin/xattr
$ podman run --it --rm --entrypoint /usr/local/bin/xattr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xattr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### activate-global-python-argcomplete

```bash
$ singularity exec <container> /usr/local/bin/activate-global-python-argcomplete
$ podman run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-argcomplete-check-easy-install-script

```bash
$ singularity exec <container> /usr/local/bin/python-argcomplete-check-easy-install-script
$ podman run --it --rm --entrypoint /usr/local/bin/python-argcomplete-check-easy-install-script   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-argcomplete-check-easy-install-script   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-argcomplete-tcsh

```bash
$ singularity exec <container> /usr/local/bin/python-argcomplete-tcsh
$ podman run --it --rm --entrypoint /usr/local/bin/python-argcomplete-tcsh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-argcomplete-tcsh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### register-python-argcomplete

```bash
$ singularity exec <container> /usr/local/bin/register-python-argcomplete
$ podman run --it --rm --entrypoint /usr/local/bin/register-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/register-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8

```bash
$ singularity exec <container> /usr/local/bin/python3.8
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.8-config

```bash
$ singularity exec <container> /usr/local/bin/python3.8-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.8-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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