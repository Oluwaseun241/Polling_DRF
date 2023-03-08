# Polling DRF

REST api with Django Rest Framework where authenticated users (Token Authentication) can create a poll

- URL: https://polling.up.railway.app/

## API Endpionts

- User registration endpoint

```
/api/auth/register
```

- User login endpoint

```
/api/auth/login
```

- Create poll:

```
/api/poll/create
```

- Fetch poll:
  Any user can fetch the poll

```
/api/poll
```

- Answer poll

Any user can answer the poll

```
/api/poll/{id}/answer
```

- Delete poll

Only the user who created the poll can delete it

```
/api/poll/{id}
```
