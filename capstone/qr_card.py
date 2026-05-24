from __future__ import annotations

from pathlib import Path

import qrcode


INFO = {
    "project_name": "AUTOSAR-Based Vehicle Speed Monitoring ECU CAN Communication & Python Test Automation",
    "capstone_project": "QR code enabled project info",
    "student_id": "55903",
    "name": "Lokesh Prabhu S",
}


def _escape_vcard(value: str) -> str:
    return (
        value.replace("\\", "\\\\")
        .replace(";", "\\;")
        .replace(",", "\\,")
        .replace("\n", "\\n")
    )


def _build_vcard(info: dict[str, str]) -> str:
    full_name = info["name"]
    project_name = _escape_vcard(info["project_name"])
    capstone_project = _escape_vcard(info["capstone_project"])
    student_id = _escape_vcard(info["student_id"])

    note = f"Capstone Project: {capstone_project}\\nStudent ID: {student_id}"

    return (
        "BEGIN:VCARD\n"
        "VERSION:3.0\n"
        f"FN:{_escape_vcard(full_name)}\n"
        f"N:{_escape_vcard(full_name)};;;;\n"
        f"TITLE:{project_name}\n"
        f"ORG:{capstone_project}\n"
        f"NOTE:{note}\n"
        "END:VCARD"
    )


def _build_plain_text(info: dict[str, str]) -> str:
    return (
        f"Project Name: {info['project_name']}\n"
        f"Capstone Project: {info['capstone_project']}\n"
        f"Student ID: {info['student_id']}\n"
        f"Name: {info['name']}"
    )


def create_qr_image(qr_data: str, output_dir: Path | str = ".", filename: str = "project_qr.png") -> Path:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=2,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")

    out_path = output_dir / filename
    qr_img.save(out_path)
    return out_path


def create_offline_qr(
    output_dir: Path | str = ".",
    filename: str = "project_qr.png",
    mode: str = "text",
) -> Path:
    if mode == "vcard":
        qr_data = _build_vcard(INFO)
    elif mode == "text":
        qr_data = _build_plain_text(INFO)
    else:
        raise ValueError("mode must be 'vcard' or 'text'")

    return create_qr_image(qr_data, output_dir=output_dir, filename=filename)


if __name__ == "__main__":
    qr_path = create_offline_qr()
    print(f"QR code: {qr_path}")
