import dns.resolver


def check_mx_records(emails):
    print(f"{'Email':<30} | {'Статус'}")
    print("-" * 60)

    for email in emails:
        if '@' not in email:
            print(f"{email:<30} | Некорректный формат email")
            continue

        domain = email.split('@')[-1]

        try:
            # найти MX-записи для домена
            records = dns.resolver.resolve(domain, 'MX')

            status = "домен валиден"

        except dns.resolver.NXDOMAIN:
            status = "домен отсутствует"

        except (dns.resolver.NoAnswer, dns.resolver.NoNameservers, dns.resolver.LifetimeTimeout):
            status = "MX-записи отсутствуют или некорректны"

        except Exception:
            status = "MX-записи отсутствуют или некорректны"

        print(f"{email:<30} | {status}")


email_list = [
    "user@google.com",
    "test@yandex.ru",
    "fake@nonexistent123.com",
    "user@example.com",
    "admin@localhost",
    "test@www.google.com",
    "mail@org"
]

check_mx_records(email_list)
