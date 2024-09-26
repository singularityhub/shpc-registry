---
layout: container
name:  "quay.io/biocontainers/nii2dcm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nii2dcm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nii2dcm/container.yaml"
updated_at: "2024-09-26 10:52:54.553185"
latest: "0.1.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/nii2dcm"
aliases:
 - "keyring"
 - "nib-conform"
 - "nib-convert"
 - "nib-dicomfs"
 - "nib-diff"
 - "nib-ls"
 - "nib-nifti-dx"
 - "nib-roi"
 - "nib-stats"
 - "nib-tck2trk"
 - "nib-trk2tck"
 - "nii2dcm"
 - "parrec2nii"
 - "pkginfo"
 - "pydicom"
 - "twine"
 - "dunamai"
 - "markdown-it"
 - "docutils"
 - "rst2html4.py"
 - "rst2html5.py"
 - "rst2html.py"
 - "rst2latex.py"
 - "rst2man.py"
 - "rst2odt.py"
 - "rst2odt_prepstyles.py"
 - "rst2pseudoxml.py"
 - "rst2s5.py"
 - "rst2xetex.py"
 - "rst2xml.py"
 - "rstpep2html.py"
 - "tjbench"
 - "pygmentize"
 - "dbus-cleanup-sockets"
 - "dbus-daemon"
 - "dbus-launch"
 - "dbus-monitor"
 - "dbus-run-session"
 - "dbus-send"
 - "dbus-test-tool"
 - "dbus-update-activation-environment"
versions:
 - "0.1.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for nii2dcm"
config: {"url": "https://biocontainers.pro/tools/nii2dcm", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for nii2dcm", "latest": {"0.1.2--pyhdfd78af_0": "sha256:b9bec833a1db2346f159cd0959d72f4fcb6e3169bca335a782074a2c54912eed"}, "tags": {"0.1.2--pyhdfd78af_0": "sha256:b9bec833a1db2346f159cd0959d72f4fcb6e3169bca335a782074a2c54912eed"}, "docker": "quay.io/biocontainers/nii2dcm", "aliases": {"keyring": "/usr/local/bin/keyring", "nib-conform": "/usr/local/bin/nib-conform", "nib-convert": "/usr/local/bin/nib-convert", "nib-dicomfs": "/usr/local/bin/nib-dicomfs", "nib-diff": "/usr/local/bin/nib-diff", "nib-ls": "/usr/local/bin/nib-ls", "nib-nifti-dx": "/usr/local/bin/nib-nifti-dx", "nib-roi": "/usr/local/bin/nib-roi", "nib-stats": "/usr/local/bin/nib-stats", "nib-tck2trk": "/usr/local/bin/nib-tck2trk", "nib-trk2tck": "/usr/local/bin/nib-trk2tck", "nii2dcm": "/usr/local/bin/nii2dcm", "parrec2nii": "/usr/local/bin/parrec2nii", "pkginfo": "/usr/local/bin/pkginfo", "pydicom": "/usr/local/bin/pydicom", "twine": "/usr/local/bin/twine", "dunamai": "/usr/local/bin/dunamai", "markdown-it": "/usr/local/bin/markdown-it", "docutils": "/usr/local/bin/docutils", "rst2html4.py": "/usr/local/bin/rst2html4.py", "rst2html5.py": "/usr/local/bin/rst2html5.py", "rst2html.py": "/usr/local/bin/rst2html.py", "rst2latex.py": "/usr/local/bin/rst2latex.py", "rst2man.py": "/usr/local/bin/rst2man.py", "rst2odt.py": "/usr/local/bin/rst2odt.py", "rst2odt_prepstyles.py": "/usr/local/bin/rst2odt_prepstyles.py", "rst2pseudoxml.py": "/usr/local/bin/rst2pseudoxml.py", "rst2s5.py": "/usr/local/bin/rst2s5.py", "rst2xetex.py": "/usr/local/bin/rst2xetex.py", "rst2xml.py": "/usr/local/bin/rst2xml.py", "rstpep2html.py": "/usr/local/bin/rstpep2html.py", "tjbench": "/usr/local/bin/tjbench", "pygmentize": "/usr/local/bin/pygmentize", "dbus-cleanup-sockets": "/usr/local/bin/dbus-cleanup-sockets", "dbus-daemon": "/usr/local/bin/dbus-daemon", "dbus-launch": "/usr/local/bin/dbus-launch", "dbus-monitor": "/usr/local/bin/dbus-monitor", "dbus-run-session": "/usr/local/bin/dbus-run-session", "dbus-send": "/usr/local/bin/dbus-send", "dbus-test-tool": "/usr/local/bin/dbus-test-tool", "dbus-update-activation-environment": "/usr/local/bin/dbus-update-activation-environment"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nii2dcm.
singularity registry hpc automated addition for nii2dcm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nii2dcm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nii2dcm:0.1.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nii2dcm/0.1.2--pyhdfd78af_0
$ module help quay.io/biocontainers/nii2dcm/0.1.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nii2dcm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nii2dcm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nii2dcm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nii2dcm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nii2dcm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nii2dcm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### keyring

```bash
$ singularity exec <container> /usr/local/bin/keyring
$ podman run --it --rm --entrypoint /usr/local/bin/keyring   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/keyring   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nib-conform

```bash
$ singularity exec <container> /usr/local/bin/nib-conform
$ podman run --it --rm --entrypoint /usr/local/bin/nib-conform   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nib-conform   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nib-convert

```bash
$ singularity exec <container> /usr/local/bin/nib-convert
$ podman run --it --rm --entrypoint /usr/local/bin/nib-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nib-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nib-dicomfs

```bash
$ singularity exec <container> /usr/local/bin/nib-dicomfs
$ podman run --it --rm --entrypoint /usr/local/bin/nib-dicomfs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nib-dicomfs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nib-diff

```bash
$ singularity exec <container> /usr/local/bin/nib-diff
$ podman run --it --rm --entrypoint /usr/local/bin/nib-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nib-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nib-ls

```bash
$ singularity exec <container> /usr/local/bin/nib-ls
$ podman run --it --rm --entrypoint /usr/local/bin/nib-ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nib-ls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nib-nifti-dx

```bash
$ singularity exec <container> /usr/local/bin/nib-nifti-dx
$ podman run --it --rm --entrypoint /usr/local/bin/nib-nifti-dx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nib-nifti-dx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nib-roi

```bash
$ singularity exec <container> /usr/local/bin/nib-roi
$ podman run --it --rm --entrypoint /usr/local/bin/nib-roi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nib-roi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nib-stats

```bash
$ singularity exec <container> /usr/local/bin/nib-stats
$ podman run --it --rm --entrypoint /usr/local/bin/nib-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nib-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nib-tck2trk

```bash
$ singularity exec <container> /usr/local/bin/nib-tck2trk
$ podman run --it --rm --entrypoint /usr/local/bin/nib-tck2trk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nib-tck2trk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nib-trk2tck

```bash
$ singularity exec <container> /usr/local/bin/nib-trk2tck
$ podman run --it --rm --entrypoint /usr/local/bin/nib-trk2tck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nib-trk2tck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nii2dcm

```bash
$ singularity exec <container> /usr/local/bin/nii2dcm
$ podman run --it --rm --entrypoint /usr/local/bin/nii2dcm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nii2dcm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parrec2nii

```bash
$ singularity exec <container> /usr/local/bin/parrec2nii
$ podman run --it --rm --entrypoint /usr/local/bin/parrec2nii   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parrec2nii   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pkginfo

```bash
$ singularity exec <container> /usr/local/bin/pkginfo
$ podman run --it --rm --entrypoint /usr/local/bin/pkginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pkginfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydicom

```bash
$ singularity exec <container> /usr/local/bin/pydicom
$ podman run --it --rm --entrypoint /usr/local/bin/pydicom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydicom   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### twine

```bash
$ singularity exec <container> /usr/local/bin/twine
$ podman run --it --rm --entrypoint /usr/local/bin/twine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/twine   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dunamai

```bash
$ singularity exec <container> /usr/local/bin/dunamai
$ podman run --it --rm --entrypoint /usr/local/bin/dunamai   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dunamai   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown-it

```bash
$ singularity exec <container> /usr/local/bin/markdown-it
$ podman run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### docutils

```bash
$ singularity exec <container> /usr/local/bin/docutils
$ podman run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html4.py

```bash
$ singularity exec <container> /usr/local/bin/rst2html4.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html4.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html4.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html5.py

```bash
$ singularity exec <container> /usr/local/bin/rst2html5.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html5.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html5.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html.py

```bash
$ singularity exec <container> /usr/local/bin/rst2html.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2latex.py

```bash
$ singularity exec <container> /usr/local/bin/rst2latex.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2latex.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2latex.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2man.py

```bash
$ singularity exec <container> /usr/local/bin/rst2man.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2man.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2man.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2odt.py

```bash
$ singularity exec <container> /usr/local/bin/rst2odt.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2odt.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2odt.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2odt_prepstyles.py

```bash
$ singularity exec <container> /usr/local/bin/rst2odt_prepstyles.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2odt_prepstyles.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2odt_prepstyles.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2pseudoxml.py

```bash
$ singularity exec <container> /usr/local/bin/rst2pseudoxml.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2pseudoxml.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2pseudoxml.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2s5.py

```bash
$ singularity exec <container> /usr/local/bin/rst2s5.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2s5.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2s5.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2xetex.py

```bash
$ singularity exec <container> /usr/local/bin/rst2xetex.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2xetex.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2xetex.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2xml.py

```bash
$ singularity exec <container> /usr/local/bin/rst2xml.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2xml.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2xml.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rstpep2html.py

```bash
$ singularity exec <container> /usr/local/bin/rstpep2html.py
$ podman run --it --rm --entrypoint /usr/local/bin/rstpep2html.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rstpep2html.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pygmentize

```bash
$ singularity exec <container> /usr/local/bin/pygmentize
$ podman run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pygmentize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbus-cleanup-sockets

```bash
$ singularity exec <container> /usr/local/bin/dbus-cleanup-sockets
$ podman run --it --rm --entrypoint /usr/local/bin/dbus-cleanup-sockets   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbus-cleanup-sockets   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbus-daemon

```bash
$ singularity exec <container> /usr/local/bin/dbus-daemon
$ podman run --it --rm --entrypoint /usr/local/bin/dbus-daemon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbus-daemon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbus-launch

```bash
$ singularity exec <container> /usr/local/bin/dbus-launch
$ podman run --it --rm --entrypoint /usr/local/bin/dbus-launch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbus-launch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbus-monitor

```bash
$ singularity exec <container> /usr/local/bin/dbus-monitor
$ podman run --it --rm --entrypoint /usr/local/bin/dbus-monitor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbus-monitor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbus-run-session

```bash
$ singularity exec <container> /usr/local/bin/dbus-run-session
$ podman run --it --rm --entrypoint /usr/local/bin/dbus-run-session   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbus-run-session   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbus-send

```bash
$ singularity exec <container> /usr/local/bin/dbus-send
$ podman run --it --rm --entrypoint /usr/local/bin/dbus-send   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbus-send   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbus-test-tool

```bash
$ singularity exec <container> /usr/local/bin/dbus-test-tool
$ podman run --it --rm --entrypoint /usr/local/bin/dbus-test-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbus-test-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbus-update-activation-environment

```bash
$ singularity exec <container> /usr/local/bin/dbus-update-activation-environment
$ podman run --it --rm --entrypoint /usr/local/bin/dbus-update-activation-environment   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbus-update-activation-environment   -v ${PWD} -w ${PWD} <container> -c " $@"
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