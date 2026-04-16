FROM fedora:38 AS builder

RUN dnf install -y rpm-build zip && dnf clean all

# Copy scripts and spec
COPY ["Ping LLDP neighbor/ping_lldp_neighbor-sysName.py", "/build/scripts/"]
COPY ["Ping LLDP neighbor/ping_lldp_neighbor-mgmtAddress.py", "/build/scripts/"]
COPY ["Ping LLDP neighbor/pingLldpIP.spec", "/root/rpmbuild/SPECS/"]

# Create source tarball expected by the spec
RUN mkdir -p /root/rpmbuild/{SOURCES,BUILD,RPMS,SRPMS} && \
    mkdir /build/pingLldpIP && \
    cp /build/scripts/*.py /build/pingLldpIP/ && \
    tar -czf /root/rpmbuild/SOURCES/pingLldpIP.tar.gz -C /build pingLldpIP/

# Build RPM
RUN rpmbuild -ba /root/rpmbuild/SPECS/pingLldpIP.spec

# Create SWIX: zip of RPM + manifest.txt with SHA1
RUN set -e && \
    RPM_FILE=$(find /root/rpmbuild/RPMS -name "*.rpm" | head -1) && \
    RPM_NAME=$(basename "$RPM_FILE") && \
    VERSION=$(rpm -qp --queryformat '%{VERSION}-%{RELEASE}' "$RPM_FILE") && \
    SWIX_NAME="pingLldpIP-${VERSION}.noarch.swix" && \
    SHA1=$(sha1sum "$RPM_FILE" | awk '{print $1}') && \
    mkdir -p /swix && \
    cp "$RPM_FILE" /swix/ && \
    printf "format: 1\nprimaryRpm: %s\n%s-sha1: %s\n" \
        "$RPM_NAME" "$RPM_NAME" "$SHA1" > /swix/manifest.txt && \
    cd /swix && \
    zip "$SWIX_NAME" manifest.txt "$RPM_NAME" && \
    ln -s "$SWIX_NAME" latest.swix

# Export stage — only the SWIX file
FROM scratch AS artifact
COPY --from=builder /swix/ /
