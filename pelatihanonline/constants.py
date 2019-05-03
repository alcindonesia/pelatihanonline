SUBJECT_CHOICES = (
    ('MAT', 'Matematika SMA'),
    ('FIS', 'Fisika SMA'),
    ('KIM', 'Kimia SMA'),
    ('BIO', 'Biologi SMA'),
    ('KOM', 'Komputer SMA'),
    ('AST', 'Astronomi SMA'),
    ('GEO', 'Geografi SMA'),
    ('EKO', 'Ekonomi SMA'),
    ('KEB', 'Kebumian SMA'),
    ('MAP', 'Matematika SMP'),
    ('BIP', 'Biologi SMP'),
    ('FIP', 'Fisika SMP'),
    ('IPS', 'IPS SMP'),
)

def get_full_subject(short):
    for subject in SUBJECT_CHOICES:
        if short == subject[0]:
            return subject[1]
    return ""

ANSWER_CHOICES = (
    ('-', '-'),
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E'),
)

ROLE_CHOICES = (
    ('SIS', 'Siswa'),
    ('GUR', 'Guru'),
)
